#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();

my $username = $cgi->param('username');
my $password1 = $cgi->param('password1');
my $password2 = $cgi->param('password2');

if ($password1 == $password2) {
    print "username: $username, password: $password1";
} else {
    print "password mismatch, try again!";
}


