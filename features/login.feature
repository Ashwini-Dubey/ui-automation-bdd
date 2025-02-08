Feature: Login Functionality

    Scenario: Test the sucessful login to the SauceDemo Web Application.

        Given the user is on the login page
        When the user enters the valid credentials
        And clicks the login button
        Then user should be redirected to the Dashboard
