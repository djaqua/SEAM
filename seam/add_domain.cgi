#!/usr/bin/perl

use CGI;

require "seam-lib.pl";
require "pjsmanager.pl";


my $cgi = CGI->new();

$domainName = $cgi->param('domainName');
$actionBtn = $cgi->param('actionBtn');

if ($text{'proceed'} eq $actionBtn) {
    
    # TODO sanitize $domainName
   
    $domain = add_domain( $domainName );
    
    redirect("edit_domain.cgi?dId=$domain->{id}");
     
} elsif ($text{'cancel'} eq $actionBtn) {
    
    redirect("index.cgi");

} elsif ("" eq $actionBtn) {

    ui_print_header( undef, $text{'add_domain_title'}, undef );
    
    print &ui_form_start("add_domain.cgi");

    print &ui_textbox("domainName");
    pjsmanager::exampleInputText("domainName", "example.net");          
    # TODO: autoexample with pjsmanager 

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    print pjsmanager::compile(1); 
    &ui_print_footer("index.cgi", $text{'edit_mailserver_title'});
} 

