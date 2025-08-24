# API Automation Project

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-tested-brightgreen)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/allure-report-blueviolet)](https://docs.qameta.io/allure/)

## Project Overview
Automates testing of public APIs from [AutomationExercise](https://automationexercise.com).  
Covers:

- Product listing (GET/POST)
- Brand listing (GET/PUT)
- User login verification (POST/DELETE)
- User account management (Create, Update, Delete, Get details)

Tests are written in **Python** using `pytest` and `requests`. Detailed reports are generated with **Allure**.

## Project Structure
api_automation/
├── .idea/ # PyCharm config
├── .venv/ # Python virtual environment
├── reports/ # Allure reports
├── tests/ # Pytest test cases
├── utilities/ # Helper scripts & test data
├── api_test_cases.xlsx # Test case scenarios
├── properties.ini # API endpoint configuration
├── run.bat # Batch file to run tests & reports
└── pycache/ # Python cache

bash
Copy
Edit

## Setup
```bash
git clone <repo-url>
cd api_automation
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
Running Tests
Run all tests and generate Allure reports:

bash
Copy
Edit
run.bat
Reports will be in reports/ folder. Pass/fail results, API responses, and test details are logged.

Notes
Order of user account tests is important: Create → Get → Update → Delete

GET requests use params; POST/PUT/DELETE use data or json

Random emails are generated for account creation to avoid duplicates

pgsql
Copy
Edit
