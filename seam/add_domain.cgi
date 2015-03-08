#!/usr/bin/perl

require "seam-lib.pl";
require "pjsmanager.pl";

&ReadParse();

if ($text{'proceed'} eq $in{actionBtn}) {
    
    # TODO sanitize $domainName
   
    $domain = add_domain( $in{domainName} );
    
    redirect("edit_domain.cgi?dId=$domain->{id}");
     
} elsif ($text{'cancel'} eq $in{actionBtn}) {
    
    redirect("index.cgi");

} else {

    ui_print_header( undef, $text{'add_domain_title'}, undef );
    
    print &ui_form_start("add_domain.cgi");

    print &ui_textbox("domainName");
    pjsmanager::exampleInputText("domainName", "example.net");          

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    print pjsmanager::compile(1); 
    &ui_print_footer("index.cgi", $text{'edit_mailserver_title'});
} 

