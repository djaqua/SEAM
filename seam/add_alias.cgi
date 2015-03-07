#!/usr/bin/perl


require "seam-lib.pl";
require "pjsmanager.pl";

&ReadParse();

$user = get_user_by_id( $in{uId} );
$actionBtn = $in{'actionBtn'};

if ($text{'proceed'} eq $actionBtn) {
   
    # TODO sanitize destination address 
    # TODO add forwarding address 
    #$user = add_user( $userName, $domainId, "" );
   
     
    #ui_print_header( undef, $text{'add_user_title'}, "SEAM", undef, 1, 1 );
    #print "Destination: $in{destination}";

    add_forwarder( $user->{domain}, $user->{username}, $in{destination} );
    
    redirect( "edit_user.cgi?uId=$in{uId}" );
     
} elsif ($text{'cancel'} eq $actionBtn) {

    redirect( "edit_user.cgi?uId=$in{uId}" );

} elsif ("" eq $actionBtn) {

    ui_print_header( undef, $text{'add_user_title'}, "SEAM", undef, 1, 1 );

    # TODO use user id to get user to get domain id 

    print &ui_form_start("add_alias.cgi");

    #print &ui_hidden( "dId", $user->{domain} );
    print &ui_hidden( "uId", $in{uId} );
 
    print &ui_textbox("destination", undef, 32, 0, 32, 'id="destination"' );
    pjsmanager::exampleInputText("destination", "user\@gmail.com");          

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );
    
    print pjsmanager::compile(1);
    &ui_print_footer( "edit_user.cgi?uId=$in{uId}", 
                      $text{'edit_user_title'});

} 

