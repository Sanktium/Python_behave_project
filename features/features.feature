Feature: Heading on Selenium Webdriver Tutorial page

  Scenario: Verify heading presence on Selenium Webdriver Tutorial page
    Given Launch chrome browser
    When Open Selenium Webdriver Tutorial page
    Then Verify that the heading is present on page
    And Close browser
