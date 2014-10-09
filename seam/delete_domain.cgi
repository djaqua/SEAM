#!/usr/bin/perl                                                                 
                                                                                
require './seam-lib.pl';                                                        
                                                                                
&ReadParse();                                                                   
                                                                                
@domains = split(/\0/, $in{'dId'});                                             
                                                                                
if ($text{domains_delete} eq $in{actionBtn}) {                                  
                                                                                
    &ui_print_header( undef, $text{'delete_domain_title'}, "SEAM", undef, 1
                                                                                
    print &ui_form_start( "delete_domain.cgi" );                                
                                                                                
    for my $dId (@domains) {                                                    
        print &ui_hidden( "dId", $dId );                                        
    } 

    # TODO build a string of domain names selected for deletion                                                                          
    print qq~ <p>WARNING: You are about to delete the domain $domain->{name}.</p
            ~;                                                                  
    print &ui_form_end( [[ "actionBtn", $text{proceed}],                        
                         [ "actionBtn", $text{cancel}]] );                      
                                                                                
    &ui_print_footer( "", $text{'index_return'},);                         
                                                                                
} elsif ($text{proceed} eq $in{actionBtn}) {                                    
                                                                                
    for my $dId (@domains) {                                                    
        delete_domain( $dId );                                                  
    }                                                                           
    redirect("index.cgi");                                                      
                                                                                
} elsif ($text{cancel} eq $in{actionBtn}) {                                     
                                                                                
    redirect("index.cgi");                                                      
}                                                                               

