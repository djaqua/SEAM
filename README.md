SEAM
====
Simple Email Administration Module for Webmin/Virtualmin.

Features
========
* Add & Delete Mailserver Domains

* Add & Delete Mailserver Domain Users 

* Update Passwords for Users

* Add & Delete Aliases (Forwarding Addresses) for Users

* Edit Auto-Responders for Users

Functional Requirements
=======================
* JavaScript enhanced - functionality is only enhanced by JavaScript, not 
    dependent (eg, always a button to submit forms manually)
    
* Intuitive - no opportunities for user misinterpretation in the absence of 
    JavaScript capabilities. 

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

* Add alias return-to text not showing up

* Delete alias (0+) + Cancel causes perl execution failure 
  in seam-lib.pl at line 329 (uId not being passed along)

Project Hints
=============
* Use Case Diagram is an https://www.draw.io project
   
