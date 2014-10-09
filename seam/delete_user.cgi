#!/usr/bin/perl


require 'seam-lib.pl';

&ReadParse();

@users = split(/\0/, $in{'uId'});   

my $delete_user_sql = qq~ DELETE FROM virtual_users WHERE id=__ID__ ~;


#local $user = get_user_by_id($in{'uId'});

if ($text{'proceed'} eq $in{'actionBtn'}) {
    
    &ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);

#    print "Deleting uIds from '$in{uId}'";        
    for my $uId (@users) {
#        print "Deleting user with id '$uId'";
        local $sql = $delete_user_sql;
        if ($sql =~ s/__ID__/$uId/g) {
            print "Deleting user with id '$uId'";
            local $stmt = get_database()->prepare( $sql );
            $stmt->execute or die qq~
                "Whoops, $DBI::errstr";
            ~;
            $stmt->finish();
        }
    }
     
#    redirect("edit_mailserver.cgi");    
    
#    &ui_print_footer( "edit_mailserver.cgi?dId=$user->{domain}", $text{'index_return'},);
   
} elsif ($text{cancel} eq $in{actionBtn}) {
    redirect("edit_mailserver.cgi?dId=$user->{domain}");
} else {
    &ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 
    print &ui_form_start( "delete_user.cgi" );
    
    for my $uId (@users) {
        print &ui_hidden( "uId", $uId );

    }
    print qq~WARNING: you are about to permanently delete the following users:~;
    # TODO build string of usernames
    print &ui_form_end( [[ "actionBtn", $text{'proceed'}],
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer( "edit_mailserver.cgi?dId=$user->{domain}", $text{'index_return'},);
}


 

0
