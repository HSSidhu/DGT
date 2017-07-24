Feature: Creating an Arrangement and Booking the Deceased in EDINBURGH

  Scenario Outline: Regression Scenario for creating the Funeral for Edinburgh HUB
    Given We have created First Call <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <hub>
    And I have booked IN the deceased <Environment> <deceased_sitename> <Deceased_FirstName> <Deceased_Lastname> <hub>
    And I have completed the Mortuary Flow <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>
    And I create an event in the calendar <Deceased_FirstName> <Deceased_Lastname> <Environment> <event_type> <hub>
    Then I completed the booking out Flow <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <deceased_sitename> <hub>
    And Deceased is comitted Successfully <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>

    Examples: Edinburgh - Burial
      |Environment|event_type|Funeral_Home|Deceased_FirstName|Deceased_Lastname|funeral_type|deceased_sitename| hub|
      |local      |Funeral  |Colinton        |Karol              |Bran          |Burial       |East        |Edinburgh|


  Scenario Outline: Regression Scenario for creating the Funeral for BOLTON
    Given We have created First Call <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <hub>
    And I have booked IN the deceased <Environment> <deceased_sitename> <Deceased_FirstName> <Deceased_Lastname> <hub>
    And I have completed the Mortuary Flow <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>
    And I create an event in the calendar <Deceased_FirstName> <Deceased_Lastname> <Environment> <event_type> <hub>
    Then I completed the booking out Flow <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <deceased_sitename> <hub>
    And Deceased is comitted Successfully <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>

    Examples: Bolton - Burial
      |Environment|event_type|Funeral_Home|Deceased_FirstName|Deceased_Lastname|funeral_type|deceased_sitename| hub|
      |local      |Funeral  |Bolton        |Val              |Bran          |Burial       |Arden        |Bolton|
