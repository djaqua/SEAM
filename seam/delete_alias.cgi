#!/usr/bin/perl


require "seam-lib.pl";
require "pjsmanager.pl";

&ReadParse();

$actionBtn = $in{'actionBtn'};

if ($text{'proceed'} eq $actionBtn) {
  
#    delete_alias( $in{aId} );
    redirect("edit_user.cgi?uId=$in{uId}");
     
} elsif ($text{'cancel'} eq $actionBtn) {
    
    redirect("edit_user.cgi?uId=$in{uId}");

} else {

    ui_print_header( undef, $text{'delete_alias_title'}, "SEAM", undef, 1, 1 );


    print &ui_form_start("delete_alias.cgi");

    print "TODO: functionality";

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );
    
    &ui_print_footer( "edit_user.cgi?uId=$user->{id}", 
                      $text{'edit_user_title'});

} 

