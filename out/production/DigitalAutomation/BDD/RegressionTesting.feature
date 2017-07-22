Feature: Creating an Arrangement and Booking the Deceased

  Scenario Outline: Regression Scenario for creating the Funeral for Edinburgh HUB
    Given We have created First Call <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <hub>
    And I have booked IN the deceased <Environment> <deceased_sitename> <Deceased_FirstName> <Deceased_Lastname> <hub>
    And I have completed the Mortuary Flow <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>
    And I create an event in the calendar <Deceased_FirstName> <Deceased_Lastname> <Environment> <event_type> <hub>
    Then I completed the booking out Flow <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <deceased_sitename> <hub>
    And Deceased is comitted Successfully <Deceased_FirstName> <Deceased_Lastname> <Environment> <hub>

    Examples: Edinburgh - Burial
      |Environment|event_type|Funeral_Home|Deceased_FirstName|Deceased_Lastname|funeral_type|deceased_sitename| hub|
      |local      |Funeral  |Colinton        |Tarra4              |Fitz3          |Burial       |East        |Edinburgh|


#
#
#  Scenario Outline: Regression Scenario for creating the Funeral for BOLTON HUB
#    Given We have created First Call <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <hub>
#      |email|password|
#      |boltonuser.fd15@coopdigital.co.uk|Password99!|
#    And I have booked IN the deceased <Environment> <deceased_sitename> <Deceased_FirstName> <Deceased_Lastname>
#      |email1|email2|password|
#      |boltonuser.fd15@coopdigital.co.uk|boltonuser.fso15@coopdigital.co.uk|Password99!|
#    And I have completed the Mortuary Flow <Deceased_FirstName> <Deceased_Lastname> <Environment>
#      |email1|email2|password|
#      |boltonuser.fd15@coopdigital.co.uk|boltonuser.fso15@coopdigital.co.uk|Password99!|
#    And I create an event in the calendar <Deceased_FirstName> <Deceased_Lastname> <Environment> <event_type>
#      |email|password|
#      |boltonuser.fd15@coopdigital.co.uk|Password99!|
#    Then I completed the booking out Flow <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <Environment> <deceased_sitename>
#      |email1|email2|password|
#      |boltonuser.fd15@coopdigital.co.uk|boltonuser.fso15@coopdigital.co.uk|Password99!|
#    And Deceased is comitted Successfully <Deceased_FirstName> <Deceased_Lastname> <Environment>
#      |email|password|
#      |boltonuser.fd15@coopdigital.co.uk|Password99!|
#
#    Examples: BOLTON - Burial
#      |Environment|event_type|Funeral_Home|Deceased_FirstName|Deceased_Lastname|funeral_type|deceased_sitename|hub|
#      |local      |Funeral  |Bolton        |Adeline              |Bran          |Burial       |Arden        |Bolton|
