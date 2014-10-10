#!/usr/bin/perl


require 'seam-lib.pl';

&ReadParse();

@users = split(/\0/, $in{'uId'});   

my $delete_user_sql = qq~ DELETE FROM virtual_users WHERE id=__ID__ ~;


if ($text{'proceed'} eq $in{'actionBtn'}) {
    
    local $user = get_user_by_id( @users[0] );
    
    for my $uId (@users) {
  
        local $sql = $delete_user_sql;
  
        if ($sql =~ s/__ID__/$uId/g) {
            local $stmt = get_database()->prepare( $sql );
            $stmt->execute or die qq~
                "Whoops, $DBI::errstr";
            ~;
            $stmt->finish();
        }
    }
     
    redirect("edit_domain.cgi?dId=$user->{domain}");    
   
} elsif ($text{cancel} eq $in{actionBtn}) {

    redirect("edit_mailserver.cgi?dId=$user->{domain}");

} else {
    &ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 
    print &ui_form_start( "delete_user.cgi" );
    
    for my $uId (@users) {
        print &ui_hidden( "uId", $uId );
    }
    
    # TODO build string of usernames
    print qq~WARNING: you are about to permanently delete the following users:~;

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}],
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer( "edit_mailserver.cgi?dId=$user->{domain}", $text{'index_return'},);
}
 

