from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    xss_vulnerable = db.Column(db.Boolean, default=False)
    sql_injection_vulnerable = db.Column(db.Boolean, default=False)
    csrf_protected = db.Column(db.Boolean, default=False)
