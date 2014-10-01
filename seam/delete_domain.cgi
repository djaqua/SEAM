#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();


local $domain = $cgi->param( 'domain_id' );
local $action = $cgi->param( 'actionBtn' );

if ($text{'domains_delete'} eq $action) {

    print &ui_form_start( "delete_domain.cgi" );
    print &ui_hidden( "domain", $domain );
    print &ui_form_end( [[ "actionBtn", $text{'domains_delete_confirm'}]] );
    
} elsif ($text{'domains_delete_confirm'} eq $action) {
    
    # TODO delete the domain
    print "TODO: write SQL to delete a domain";
}



print ui_print_footer( "", $text{'index_return'},);

 


