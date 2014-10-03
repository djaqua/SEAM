#!/usr/bin/perl

use CGI;

require "seam-lib.pl";


my $cgi = CGI->new();

$domainName = $cgi->param('domainName');
$actionBtn = $cgi->param('actionBtn');

if ($text{'domains_add_proceed'} eq $actionBtn) {
    
    # TODO sanitize $domainName
   
    $domain = add_domain( $domainName );
    
    redirect("edit_domain.cgi?domain_id=$domain->{id}");
     
} elsif ($text{'cancel'} eq $actionBtn) {
    
    redirect("index.cgi");

} elsif ("" eq $actionBtn) {

    ui_print_header( undef, $text{'add_domain_title'}, "SEAM", undef, 1, 1 );
    
    print &ui_form_start("add_domain.cgi");

    print &ui_textbox("domainName");
    # TODO: autoexample with pjsmanager 

    print &ui_form_end( [[ "actionBtn", $text{'domains_add_proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer("index.cgi", $text{'add_domain_return'});
} 

