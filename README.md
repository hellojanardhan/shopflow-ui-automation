# Shopflow UI Automation

Python UI automation project using Playwright and pytest to exercise the login flow.

## Requirements

- Python
- pip

## Setup

Create and activate a virtual environment in PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the Python dependencies and Chromium browser:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Configuration

Create a `.env` file in the project root with the application URL and login credentials:

```dotenv
BASE_URL=https://www.saucedemo.com/
SAUCEDEMO_USERNAME=your_username
SAUCEDEMO_PASSWORD=your_password
LOCKED_USER=locked_out_user
```

Keep `.env` local; it is excluded from version control.

The automation logs entered field values, including the password, to the console
and `logs/automation.log`. Use test-only credentials; do not use personal or
production passwords.

## Running the tests

Run the complete test suite:

```powershell
python -m pytest
```

Run only the login tests:

```powershell
python -m pytest tests/login/test_login.py
```

The browser runs in headed mode. Pytest writes an HTML report to `reports/report.html` and Allure result files to `reports/allure-results/`.

## Project structure

```text
config/                 Environment-based application configuration
pages/                  Base and login page objects
tests/
  login/                Login test cases
utils/                  Test data generation helpers
pytest.ini              Pytest configuration and report options
requirements.txt        Python dependencies
```