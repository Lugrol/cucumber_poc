# -- This is an example of using Cucumber to test Web GUI with with Selenium WebDriver
Feature: Login

	@fixture.lauch.firefox
	Scenario: Valid login
		Given the login page is open
		When the user log in with valid credentials
		Then the inventory page is shown

	@fixture.lauch.firefox
	Scenario Outline: Invalid login
		Given the login page is open
		When the user log in with <invalid credentials>
		Then an <invalid credentials> error is shown

		Examples: 
			|invalid credentials	|
			|empty username		|
			|empty password		|
			|invalid username	|
			|invalid password	|
			|locked out user	|
	
	@fixture.lauch.firefox
	Scenario: Access without login
		Given the login page is open
		And the user is not logged in
		When the user navigates to inventory page
		Then an not logged in error is shown
