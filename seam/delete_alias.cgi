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
  
#TODO    delete_alias( $in{aId} );
   redirect("edit_user.cgi?uId=$user->{id}");

    
} elsif ($text{'cancel'} eq $actionBtn) {

    redirect("edit_user.cgi?uId=$user->{id}");

} else {

    ui_print_header( undef, $text{'delete_alias_title'}, "SEAM", undef, 1, 1 );


    print &ui_form_start("delete_alias.cgi");

    print "TODO: functionality";

    for my $aId (@alias_ids) {
        print &ui_hidden( "aId", $aId );

    }

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );
    
    &ui_print_footer( "edit_user.cgi?uId=$user->{id}", 
                      $text{'edit_user_title'});

} 

