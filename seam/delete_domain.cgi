#!/usr/bin/perl


require 'seam-lib.pl';

&ReadParse();

#@users = split(/\0/, $in{'uId'});   
@domains = split(/\0/, $in{'dId'});

#my $delete_user_sql = qq~ DELETE FROM virtual_users WHERE id=__ID__ ~;

if ($text{'proceed'} eq $in{'actionBtn'}) {
    
    &ui_print_header( "", $text{'delete_domain_title'}, "SEAM", undef, 1, 1);
    

    for my $dId (@domains) {

        delete_domain( $dId );
         
        #local $sql = $delete_domain_sql;
  
        #print "Delete domain sql: $delete_domain_sql\n";
        
        #if ($sql =~ s/__ID__/$dId/g) {
        #    local $stmt = get_database()->prepare( $sql );
        #    $stmt->execute or die qq~
        #        "Whoops, $DBI::errstr";
        #    ~;
        #    $stmt->finish();
        #}
    }
     
    redirect("index.cgi");    
   
} elsif ($text{cancel} eq $in{actionBtn}) {

    local $user = get_user_by_id( @users[0] );
    redirect("edit_domain.cgi?dId=$user->{domain}");

} else {

    &ui_print_header( "", $text{'delete_domain_title'}, "SEAM", undef, 1, 1);

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
    print qq~ <p>WARNING: You are about to delete the following domains: $domainNames</p>
            ~;                                                                  
    print &ui_form_end( [[ "actionBtn", $text{proceed}],                       
                         [ "actionBtn", $text{cancel}]] );                      
                                                                                
    &ui_print_footer( "", $text{'index_return'},);        
 
}
 

