#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

 

my $cgi = CGI->new();

local $domain_id = $cgi->param('domain_id');
local $domain = get_domain_by_id( $domain_id );
local $action = $cgi->param( 'actionBtn' );

if ($text{domains_delete} eq $action) {

    print ui_print_header( "", $text{'delete_domain_title'}, "SEAM", undef, 1, 1);
    
    print &ui_form_start( "delete_domain.cgi" );

    # TODO add support for deleting multiple domains
    print qq~ <p>WARNING: You are about to delete the domain $domain->{name}.</p>
            ~;
    print &ui_hidden( "domain_id", $domain->{id} );
    print &ui_form_end( [[ "actionBtn", $text{'domains_delete_confirm'}],
                         [ "actionBtn", $text{cancel}]] );
    
    print ui_print_footer( "", $text{'index_return'},);
    
} elsif ($text{domains_delete_confirm} eq $action) {

    delete_domain( $domain->{id} );
    redirect("index.cgi");    

} elsif ($text{cancel} eq $action) {
    
    redirect("index.cgi");    
}




 


