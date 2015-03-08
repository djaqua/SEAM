#!/usr/bin/perl

require 'seam-lib.pl';

&ReadParse();

@domains = split(/\0/, $in{'dId'});


if ($text{'proceed'} eq $in{'actionBtn'}) {

    for my $dId (@domains) {

        delete_domain( $dId );
    }
     
    redirect("index.cgi");    
   
} elsif ($text{cancel} eq $in{actionBtn}) {

    redirect("index.cgi");

} else {

    &ui_print_header( undef, $text{'delete_domain_title'}, undef );

    print &ui_form_start( "delete_domain.cgi" );                               

    local $domainNames = "";                                                      
                                                                                
    local $domain;                                                                
                                                                                
    for my $dId (@domains) {                                                      
        print &ui_hidden( "dId", $dId );                                        
        $domain = get_domain_by_id( $dId );                                         
        $domainNames .= "$domain->{name}" . ", ";                               
    }                                                                           
                                                                                
    $domainNames = substr( $domainNames, 0, length($domainNames)-2 );      

    # TODO build a string of domain names selected for deletion                 
    print qq~<b>WARNING</b>: You are about to permanently delete the following
             domains: $domainNames
            ~;                                                                  
    print &ui_form_end( [[ "actionBtn", $text{proceed}],                       
                         [ "actionBtn", $text{cancel}]] );                      
                                                                                
    &ui_print_footer( "index.cgi", $text{'edit_mailserver_title'},);        
 
}
 

