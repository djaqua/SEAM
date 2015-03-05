#!/usr/bin/perl

require 'seam-lib.pl';

&ReadParse();

@users = split(/\0/, $in{'uId'});   

if ($text{'proceed'} eq $in{'actionBtn'}) {
    
    local $user = get_user_by_id( @users[0] );
    
    for my $uId (@users) {
        delete_user( $uId );
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
        $usernames .= "$user->{username}" . ", ";
    }

    $usernames = substr( $usernames, 0, length($usernames)-2 );
    print qq~<b>WARNING</b>: you are about to permanently delete the following
             users: <i>$usernames</i>~;

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}],
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer( "edit_domain.cgi?dId=$user->{domain}", $text{edit_domain_title},);
}
 

