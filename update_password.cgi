#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();

my $user = $cgi->param('user');
my $password1 = $cgi->param('password1');
my $password2 = $cgi->param('password2');

if ($password1 eq $password2) {
#   print $username; 
   update_password($user, $password1);
   print "Password updated successfully.";    
} else {
    # TODO: come back and do this with AJAX
    print "password mismatch, try again!";
}


print ui_print_footer( "", $text{'index_return'},);

get_database()->disconnect();
