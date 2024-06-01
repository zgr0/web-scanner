# Web Scanner

Web Scanner is a simple web application developed to scan for various security vulnerabilities. The application provides basic functionality to check for XSS, SQL Injection, and CSRF vulnerabilities.

## Features

- **XSS Scanning**: Scans the URL using various XSS payloads.
- **SQL Injection Scanning**: Scans the URL using common SQL Injection payloads.
- **CSRF Scanning**: Checks whether CSRF protection is present.

## Installation

Follow the steps below to run the project on your local machine.

### Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Python Requests Library

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/zgr0/web-scanner.git
    cd web-scanner
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the database and start the application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the URL you want to scan.
3. Click the button for the vulnerability you want to scan for (XSS, SQL Injection, or CSRF).
4. The results will be displayed on the screen.
