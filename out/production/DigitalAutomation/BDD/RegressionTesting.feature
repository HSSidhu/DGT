Feature: Creating an Arrangement and Booking the Deceased

  Scenario Outline: Regression Scenario for creating the Funeral
    Given We have created First Call <Funeral_Home> <Deceased_FirstName> <Deceased_Lastname> <funeral_type> <url>
    And I have booked in the deceased in the Home <deceased_sitename> <Deceased_FirstName> <Deceased_Lastname> <Location_inHouse> <url>
    And I have completed the Mortuary Flow <Deceased_FirstName> <Deceased_Lastname> <url>
    And I create an event in the calendar <Deceased_FirstName> <Deceased_Lastname> <url> <event_type>
#    Then I completed the booking out Flow


    Examples: Burial
    |Funeral_Home|deceased_sitename   |Deceased_FirstName|Deceased_Lastname|funeral_type|Location_inHouse|url|event_type|
    |Colinton    |East                |Daniel            |Bury            |Burial      |Location01      |url|Funeral |







#    Examples: Cremation
#      |Funeral_Home|deceased_sitename|Deceased_FirstName|Deceased_Lastname|funeral_type|Location_inHouse|
#      |Colinton    |"East Newington Place"|Harry          |Kenyon           |Cremation   |Location01      |



    #|Colinton   |East Newington Place|Harry            |Kenyon             |LOcation       |

