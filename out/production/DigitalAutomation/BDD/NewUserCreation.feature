# Created by SIDHU at 123/012/201212
Feature:
  # Create new user via Djang
  # Add users via ADMIN screen
  # Set Passwords for those new users
  # FD / FSO / RM / LM / mortuary

#  Edinburgh.fd@coopdigital.co.uk		Funeral service operative		Arden House		    Lothian Road
#  Edinburgh.fso@coopdigital.co.uk		Funeral director		        Horwich		        Colinton
#  Edinburgh.lm@coopdigital.co.uk		Funeral arranger		        Chorley Old Rd		Gilmerton
#  Bolton.fd@coopdigital.co.uk		    Mortuary staff		            Hall and Heyes		Morningside
#  Bolton.fso@coopdigital.co.uk		    Logistics manager		        Relphs		        South Clerk Street
#  Bolton.lm@coopdigital.co.uk		    Regional manager		        Bolton		        Ferry Road
#                                                                        Farnworth		    Queensferry Road
#                                                                        Shaw & Son		    East Newington Place
#                                                                        Hardman and McManus	Corstorphine
#                                                                        Worthingtons		Leith
#                                                                        Cheethams		    Piershill


  Scenario: Create First user Via "Django Admin"
    Given We have logged in with env
    |environment|
    |local|
#    |preprod|
#    |qa     |

    Then we create new users using Django Admin
    |location|email12|username12|lastname12|password12|
    |edinburgh|edin.fd12@coopdigital.co.uk|edinburgh|fd12|Password99!|
    |bolton|bolton.fd12@coopdigital.co.uk|bolton|fd12|Password99!|

  Scenario: Create Other users using Main app for "Edinburgh" Users
    Given I have required login detail from user created
    |environment|email12|password12|
    |local|edin.fd12@coopdigital.co.uk|Password99!|
    Then I create all the Users
    |location|email2|username2|lastname2|role|
    |edinburgh|edtestuser.fd12@coopdigital.co.uk|edtestuser|fd12|FD|
    |edinburgh|edtestuser.fso12@coopdigital.co.uk|edtestuser|fso12|FSO|
    |edinburgh|edtestuser.lm12@coopdigital.co.uk|edtestuser|lm12|LM|
    |edinburgh|edtestuser.rm12@coopdigital.co.uk|edtestuser|rm12|RM|
    |edinburgh|edtestuser.mortuary12@coopdigital.co.uk|edtestuser|mortuary12|mortuary|

  Scenario: Create Other users using Main app for "Bolton" Users
    Given I have required login detail from user created
    |environment|email12|password12|
    |local|bolton.fd12@coopdigital.co.uk|Password99!|
    Then I create all the Users
    |location|email2|username2|lastname2|role|
    |bolton|boltonuser.fd12@coopdigital.co.uk|boltonuser|fd12|FD|
    |bolton|boltonuser.fso12@coopdigital.co.uk|boltonuser|fso12|FSO|
    |bolton|boltonuser.lm12@coopdigital.co.uk|boltonuser|lm12|LM|
    |bolton|boltonuser.rm12@coopdigital.co.uk|boltonuser|rm12|RM|
    |bolton|boltonuser.mortuary12@coopdigital.co.uk|boltonuser|mortuary12|mortuary|


  Scenario: Re-set all the passwords for the created users
    Given We have logged in with env
      |environment|adminpassword|
      |local|PX3TfHt5JxW72mJnpdG7Yr4S              |
    Then I generate passwords for all the users created
    |email|password|username|lastname|
    |edtestuser.fd12@coopdigital.co.uk|Password99!|edtestuser|fd12|
    |edtestuser.fso12@coopdigital.co.uk|Password99!|edtestuser|fso12|
    |edtestuser.lm12@coopdigital.co.uk|Password99! |edtestuser|lm12 |
    |edtestuser.rm12@coopdigital.co.uk|Password99! |edtestuser|rm12 |
    |edtestuser.mortuary12@coopdigital.co.uk|Password99!|edtestuser|mortuary12|
    |boltonuser.fd12@coopdigital.co.uk|Password99!      |boltonuser|fd12      |
    |boltonuser.fso12@coopdigital.co.uk|Password99!     |boltonuser|fso12     |
    |boltonuser.lm12@coopdigital.co.uk|Password99!      |boltonuser|lm12      |
    |boltonuser.rm12@coopdigital.co.uk|Password99!      |boltonuser|rm12      |
    |boltonuser.mortuary12@coopdigital.co.uk|Password99!|boltonuser|mortuary12|

