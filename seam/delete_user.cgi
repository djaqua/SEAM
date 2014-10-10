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

    local $user = get_user_by_id( @users[0] );
    redirect("edit_domain.cgi?dId=$user->{domain}");

} else {

    &ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 
    print &ui_form_start( "delete_user.cgi" );
    
    local $usernames = "";

    local $user;
    
    for my $uId (@users) {
        print &ui_hidden( "uId", $uId );
        $user = get_user_by_id( $uId );
        $usernames .= $user->{username} . ", ";
    }

    $usernames = substr( $usernames, 0, length($usernames)-2 );
    print qq~<b>WARNING</b>: you are about to permanently delete the following
             users: <i>$usernames</i>~;

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}],
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer( "edit_domain.cgi?dId=$user->{domain}", $text{edit_domain_title},);
}
 

