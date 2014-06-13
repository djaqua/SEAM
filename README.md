SEAM
====
Simple Email Administration Module for Webmin/Virtualmin.

Features
========
* Update Passwords for Users

* Add, Edit, & Delete Forwards for Users

* Add, Edit, & Delete Auto-Responders for Users

Functional Requirements
=======================
* JavaScript enhanced - functionality is only enhanced by JavaScript, not 
    dependent (eg, always a button to submit forms manually)
    
* Intuitive - no opportunities for user misinterpretation in the absence of 
    JavaScript capabilities. 

Non-Functional Requirements
===========================
* forms are _submitted via POST_ to the script in which they are written for 
  sanitation and _redirected via GET_ to the appropriate action handler.
  - has the added benefit of centralizing the management of CGI variables and
    thus limiting the scope of their destruction.  
  - has the consequence of session-variable over-head, but not so terrible
    since this is not going to undergo frequent usage by every user. 

* _session variables_ used for script-to-script (eg index to select-user) 
  communication since _there are no POST-redirect capabilities_

* _http variables_ for script-to-self (eg index to index) communication
  since this will be the primary style of form-submission. 
  - has the added benefit of keeping sanitized variables separate from 
    dirty variables.


