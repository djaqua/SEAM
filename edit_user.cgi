#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();

my $domain = $cgi->param('domain');


if (defined $cgi->param('updatePasswordBtn')) {

    my $password1 = $cgi->param('password1');
    my $password2 = $cgi->param('password2');
    my $user = $cgi->param('user');

    if ($password1 eq $password2) {
#   print $username; 
       update_password($user, $password1);
       print "Password updated successfully.";    
       get_database()->disconnect();
    } else {
        # TODO: come back and do this with AJAX
        print "password mismatch, try again!";
    }
} elsif (defined $cgi->param('addForwarderBtn')) {
    local $source_domain = $cgi->param('domain'); 

    local $selected_user_id = $cgi->param('user');
    local $source_username = get_user_by_id($selected_user_id)->{'username'};
    local $destination_username = $cgi->param('destination');



    add_forwarder( $source_domain, $source_username, $destination_username );
    get_database()->disconnect();
    print qq~ Successfully created forward from $source_username to 
              $destination_username.<br>\n~;
}

print ui_print_footer( "", $text{'index_return'},);

 


