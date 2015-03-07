SEAM
====
Simple Email Administration Module for Webmin/Virtualmin.

Implemented Features
====================
* Add & Delete Mailserver Domains
* Add & Delete Mailserver Domain Users 
* Update Passwords for Users
* Add Aliases (Forwarding Addresses) for Users

Remaining Features & Requirements
=================================
* Delete Alias 
* Edit Auto-Responders for Users
* Any given page should indicate what domain/user is being edited

Functional Requirements
=======================
* JavaScript enhanced - functionality is only enhanced by JavaScript, not 
    dependent (eg, always a button to submit forms manually)
* Intuitive - no opportunities for user misinterpretation in the absence of 
    JavaScript capabilities. 
* Independent of specific virtual mailserver configuration (table names, column
  names, etc) 

Non-Functional Requirements
===========================
* Should be configurable to work with custom Postfix/Dovecot virtual 
    mailserver configurations 

Bugs that need to be fixed
==========================
* Should not be able to delete 0 domains

* Deleting 0 domains & Cancel does NOT cause perl execution failure; bug? 

* Should not be able to delete 0 users

* Deleting 0 users & Cancel causes perl execution failure 
  in seam-lib.pl at line 329 (uId not being passed along)

* In anticipation, should not be able to delete 0 aliases 

* Delete alias (0+) + Cancel causes perl execution failure 
  in seam-lib.pl at line 329 (uId not being passed along)

* Order seems to matter for the forms in EditUser; if Add/List/RemoveAlias 
  comes after update password, then invert/all selection scripts won't work.
    -- there's probably a way to specify which form belongs to which set of 
       JavaScript functions, if not, then perhaps submit a fixed scripting
       engine to Webmin (via Sandbox pattern)

Project Hints
=============
* Use Case Diagram is an https://www.draw.io project
   
