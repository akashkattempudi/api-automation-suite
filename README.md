# API Automation Suite

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-tested-brightgreen)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/allure-report-blueviolet)](https://docs.qameta.io/allure/)

## 📌 Project Overview
The **API Automation Suite** is a comprehensive testing framework designed to automate the validation of public APIs from [AutomationExercise](https://automationexercise.com). Utilizing Python's `pytest` framework and `requests` library, this suite ensures robust testing of various API endpoints, including product listings, brand information, and user account management.

## 🔧 Features
- **Automated API Testing**: Efficiently tests multiple API endpoints with dynamic test data.
- **Allure Reporting**: Generates detailed, timestamped HTML reports for each test run.
- **Excel Test Case Documentation**: Maintains a comprehensive Excel sheet (`api_test_cases.xlsx`) documenting all test scenarios, expected results, and actual outcomes.
- **Batch Execution**: Simplifies test execution and report generation through a convenient batch script (`run.bat`).

## 🗂 Project Structure
api-automation-suite/
├── .idea/ # PyCharm project configuration
├── .pytest_cache/ # Pytest cache
├── .venv/ # Python virtual environment
├── reports/ # Allure test reports
├── tests/ # Pytest test cases
├── utilities/ # Helper scripts and configurations
├── api_test_cases.xlsx # Test case documentation
├── properties.ini # API endpoint configurations
├── run.bat # Batch script to run tests and generate reports
└── pycache/ # Python bytecode cache

bash
Copy
Edit

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.11 or higher
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/akashkattempudi/api-automation-suite.git
   cd api-automation-suite
Set up a virtual environment:

bash
Copy
Edit
python -m venv .venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
.venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source .venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running Tests
Execute the tests and generate Allure reports:

bash
Copy
Edit
run.bat
This command will:

Run all defined test cases.

Generate Allure reports in the reports/ directory.

Open the generated report in your default web browser.

📊 Test Reports
Allure Reports: Located in the reports/ directory, these HTML reports provide a detailed overview of each test's execution, status, and logs.

Excel Documentation: The api_test_cases.xlsx file contains a structured record of all test scenarios, including:

Test Scenario ID

Test Case ID

Test Case Description

Expected Result

Actual Result

Test Status (Passed/Failed)

Test Environment

🧪 Test Data
User Data: Randomized user information is generated for account creation tests to ensure unique entries and prevent conflicts.

API Endpoints: Configured in properties.ini, allowing easy updates and management of API URLs.

🛠 Utilities
Batch Script (run.bat): Facilitates the execution of tests and report generation with a single command.

Helper Scripts: Located in the utilities/ directory, these scripts assist in tasks like generating random user data and configuring test environments.

📌 Notes
Test Execution Order: The sequence of tests is crucial, especially for user account operations. The recommended order is:

Create User

Get User Details

Update User Information

Delete User Account

API Methods: The suite tests various HTTP methods, including GET, POST, PUT, and DELETE, to ensure comprehensive API validation.

🤝 Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For inquiries or support, please reach out to akashkattempudi@gmail.com.
