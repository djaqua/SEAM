#!/usr/bin/perl


require "seam-lib.pl";
require "pjsmanager.pl";

&ReadParse();

$actionBtn = $in{'actionBtn'};

@alias_ids = split(/\0/, $in{'aId'});   
 
$alias = get_alias( $alias_ids[0] );    
 
# this seems like a terrible relationship to me; irritatingly tailored to the
# custom virtual mailserver configuration which spawned this project, which
# also defines an annoyingly redundant relationship between 
# virtual_users and virtual_aliases. While it may improve performance for the 
# actual operation of the mailserver, it hinders design on all other fronts; 
# there ~has~ to be a way to decouple the alias surce from a username
#
# TODO could be a good opportunity for a get_user_by_alias
$user = get_user_by_username( $alias->{source} );

if ($text{'proceed'} eq $actionBtn) {
  
   for my $aId (@alias_ids) {
       delete_alias( $aId  );
   }
   redirect("edit_user.cgi?uId=$user->{id}");

    
} elsif ($text{'cancel'} eq $actionBtn) {

    redirect("edit_user.cgi?uId=$user->{id}");

} else {

    local $desc = &text( 'delete_alias_desc', 
                          $user->{username} );

    &ui_print_header( $desc, $text{'delete_alias_title'}, undef );

    print &ui_form_start("delete_alias.cgi");
    
    local $alias_str = "";

    # TODO a do while loop would be awesome here, since we've already 
    # called get_alias_by_id for the first element in aId
    for my $aId (@alias_ids) {
        print &ui_hidden( "aId", $aId );

        $alias = get_alias( $aId );
        $alias_str .= "$alias->{destination}" . ", ";
    }

    $alias_str = substr( $alias_str, 0, length($alias_str)-2 );
    print qq~<b>WARNING</b>: you are about to permanently delete the following
             forwarding addresses: <i>$alias_str</i>~;


    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );
    
    &ui_print_footer( "edit_user.cgi?uId=$user->{id}", 
                      $text{'edit_user_title'});

} 

