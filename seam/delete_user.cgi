#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();

local $user = get_user_by_id($cgi->param('uId'));
local $action = $cgi->param( 'actionBtn' );

if ($text{'users_delete'} eq $action) {
    
       
    # TODO delete the user
    print "TODO: write SQL to delete a user";
   
} elsif ($text{cancel} eq $action) {
    redirect("edit_mailserver.cgi?dId=$user->{domain}");
} else {
 
    print &ui_form_start( "delete_user.cgi" );
    print &ui_hidden( "uId", $user->{id} );
    print &ui_form_end( [[ "actionBtn", $text{'proceed'}]] );
}

print ui_print_footer( "edit_mailserver.cgi?dId=$user->{domain}", $text{'index_return'},);

 


