# UI Automation BDD Framework

## 📌 Overview
This project is a **UI Automation Framework** using **Python, Selenium, and Behave (BDD)** for end-to-end web application testing. It follows the **Behavior-Driven Development (BDD)** approach using Gherkin syntax for test scenarios.

## 🚀 Tech Stack
- **Programming Language**: Python
- **Test Framework**: Behave (BDD)
- **Browser Automation**: Selenium WebDriver
- **Reporting**: Allure Reports
- **Dependency Management**: pip / virtualenv

## 📂 Project Structure
```
UI_Automation_BDD_Framework/
│── features/                   # BDD feature files
│   ├── login.feature            # Example feature file
│   ├── steps/                   # Step definitions
│   │   ├── login_steps.py       # Step implementation
│   ├── environment.py           # Hooks for setup/teardown
│── pages/                       # Page Object Model (POM)
│   ├── LoginPage.py             # Page class for Login
│── reports/                     # Test reports
│── config/                      # Configuration files
│── drivers/                     # WebDriver executables
│── run_tests.py                 # Script to execute tests
│── requirements.txt             # Project dependencies
│── README.md                    # Project documentation
```

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Ashwini-Dubey/ui-automation-bdd.git
cd ui-automation-bdd
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Download and Setup WebDriver
- Download **Chromedriver** (matching your Chrome version) from [ChromeDriver](https://chromedriver.chromium.org/downloads)
- Place it inside `drivers/` folder

### 5️⃣ Run Tests
```sh
python run_tests.py
```
OR run tests with Behave:
```sh
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

### 6️⃣ Generate Allure Report
```sh
allure generate reports/allure-results --clean -o reports/allure-report
allure serve reports/allure-report
```

## 📝 Writing Test Cases
Test cases are written in **Gherkin syntax** inside `.feature` files.
Example `features/login.feature`:
```gherkin
Feature: Login Functionality

  Scenario: Test successful login to the SauceDemo Web Application
    Given the user is on the login page
    When the user enters the valid credentials
    And clicks the login button
    Then user should be redirected to the Dashboard
```

## 📌 Contribution
Feel free to contribute by creating **issues**, submitting **pull requests**, or improving the documentation.

---
🎯 **Happy Testing!** 🚀

