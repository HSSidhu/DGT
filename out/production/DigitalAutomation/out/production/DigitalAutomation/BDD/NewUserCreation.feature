# Created by SIDHU at 153/015/201515
Feature: Create Users
  # Create new user via Djang
  # Add users via ADMIN screen
  # Set Passwords for those new users
  # FD / FSO / RM / LM / mortuary


  Scenario: Create First user Via "Django Admin"
    Given We have logged in with env
    Then we create new users using Django Admin

  Scenario Outline: Create Other users using Main app for "Edinburgh" Users
    Given I have required login detail from user created <Location>
    Then I create all the Users <Location>

    Examples: Edinburgh Data
    |Location|
    |Edinburgh|

  Scenario Outline: Create Other users using Main app for "Bolton" Users
    Given I have required login detail from user created <Location>
    Then I create all the Users <Location>

    Examples: Bolton Data
      |Location|
      |Bolton|

  Scenario: Re-set all the passwords for the created users
    Given We have logged in with env
    Then I generate passwords for all the users created




