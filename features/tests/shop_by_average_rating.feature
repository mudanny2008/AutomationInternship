# Created by danielb.mugabo at 11/28/21
Feature: Test Scenarios for average rating functionality

  Scenario: User can sort products by average rating
    Given Open Gettop Shop page
    When Click on default sorting dropdown icon
    Then Verify https://gettop.us/shop/?orderby=rating is opened



  Scenario: User can sort products by average rating
    Given Open Gettop Shop page
    When Click on default sorting dropdown icon
    Then verify that the first product has stars


  Scenario: User can sort products by average rating and can click over the arrow
    Given Open Gettop Shop page
    When Click on default sorting dropdown icon
    When Click on button 2
    When Click on left arrow
    Then Click on right arrow