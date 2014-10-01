#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();


local $user = $cgi->param( 'user_id' );
local $action = $cgi->param( 'actionBtn' );

if ($text{'users_delete'} eq $action) {

    print &ui_form_start( "delete_user.cgi" );
    print &ui_hidden( "user", $user );
    print &ui_form_end( [[ "actionBtn", $text{'users_delete_confirm'}]] );
    
} elsif ($text{'users_delete_confirm'} eq $action) {
    
    # TODO delete the user
    print "TODO: write SQL to delete a user";
}



print ui_print_footer( "", $text{'index_return'},);

 


