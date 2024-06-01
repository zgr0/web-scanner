from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    xss_vulnerable = db.Column(db.Boolean, default=False)
    sql_injection_vulnerable = db.Column(db.Boolean, default=False)
    csrf_protected = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan/xss', methods=['POST'])
def scan_xss():
    data = request.get_json()
    url = data['url']
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "'><script>alert('XSS')</script>",
        "\"/><script>alert('XSS')</script>"
    ]
    
    xss_vulnerable = False
    for payload in payloads:
        test_url = f"{url}?q={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            xss_vulnerable = True
            break

    result = ScanResult(url=url, xss_vulnerable=xss_vulnerable)
    db.session.add(result)
    db.session.commit()
    return jsonify({"url": url, "xss_vulnerable": xss_vulnerable})

@app.route('/scan/sql_injection', methods=['POST'])
def scan_sql_injection():
    data = request.get_json()
    url = data['url']
    payloads = ["'", '"', ' OR 1=1--', ' OR 1=1#', ' OR 1=1/*']
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}{payload}"
        response = requests.get(test_url)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            vulnerable = True
            break
    result = ScanResult(url=url, sql_injection_vulnerable=vulnerable)
    db.session.add(result)
    db.session.commit()
    return jsonify({"url": url, "sql_injection_vulnerable": vulnerable})

@app.route('/scan/csrf', methods=['POST'])
def scan_csrf():
    data = request.get_json()
    url = data['url']
    response = requests.get(url)
    csrf_token = '<input type="hidden" name="csrf_token"' in response.text.lower()
    result = ScanResult(url=url, csrf_protected=csrf_token)
    db.session.add(result)
    db.session.commit()
    return jsonify({"url": url, "csrf_protected": csrf_token})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
