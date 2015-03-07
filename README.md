SEAM
====
Simple Email Administration Module for Webmin/Virtualmin. Eventually, this will
be a perfectly useful and simple way for administrators to manage virtual 
mailserver domains, users, passwords, aliases, and autoresponders. For now, it
is tightly coupled to the custom Dovecot/Postfix email server from which it
was inspired. 

Implemented Features
====================
* Add & Delete Mailserver Domains
* Add & Delete Mailserver Domain Users 
* Update Passwords for Users
* Add & Delete Aliases (Forwarding Addresses) for Users

Remaining Features, Requirements, & Miscellany
==============================================
* Edit Auto-Responders for Users
* Any given page should indicate what domain/user is being edited
* EditDomain still needs to show aliases and autoresponse
* Go back and remove all the CGI dependencies and use $in{VARNAME} 
  hash built by ReadParse() 
* Go back and use better variable names -- what I have now is a mess
  of different styles and techniques as I learned along the way
* Stop relying on /root/seam.conf -- use Webmin configuration stuff
* Cancel/Proceed/Init paradigm may be simplified with a nested if-statement
  which can also help with the perl execution failures


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

* Deleting 0 users & (Proceed | Cancel) causes perl execution failure 
  in seam-lib.pl at line 329 (uId not being passed along)

* Should not be able to delete 0 aliases 
    -- deleting 0 aliases results in perl execution failure in seam-lib.pl 
       at line 215

* Order seems to matter for the forms in EditUser; if Add/List/RemoveAlias 
  comes after update password, then invert/all selection scripts won't work.
    -- there's probably a way to specify which form belongs to which set of 
       JavaScript functions, if not, then perhaps submit a fixed scripting
       engine to Webmin (via Sandbox pattern)

Project Hints
=============
* Use Case Diagram is an https://www.draw.io project
* Git repository: https://github.com/djaqua/SEAM   

Author
======
Drew Jaqua <anjaqua@gmail.com>
