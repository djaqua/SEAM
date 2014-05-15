#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();

my $username = $cgi->param('username');
my $password1 = $cgi->param('password1');
my $password2 = $cgi->param('password2');

if ($password1 eq $password2) {
    
    
} else {
    # TODO: come back and do this with AJAX
    print "password mismatch, try again!";
}


