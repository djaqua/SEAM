#!/usr/bin/perl


require "seam-lib.pl";
require "pjsmanager.pl";

&ReadParse();

if ($text{'proceed'} eq $in{actionBtn}) {
    
    # TODO sanitize $domainName
   
    $user = add_user( $in{userName}, $in{dId}, "" );
    
    redirect("edit_user.cgi?uId=$user->{id}");
     
} elsif ($text{'cancel'} eq $in{actionBtn}) {
    
    redirect("edit_domain.cgi?dId=$in{dId}");

} else {
    
    local $domain = get_domain_by_id( $in{dId} );

    local $desc = &text( 'add_user_desc', $domain->{name} );
    &ui_print_header( $desc, $text{'add_user_title'}, undef );
    
    print &ui_form_start("add_user.cgi");

    print &ui_hidden("dId", $in{dId});
    
    print &ui_textbox("userName", undef, 32, 0, 32, 'id="userName"' );
    
    pjsmanager::exampleInputText("userName", "user\@$domain->{name}");          

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    print pjsmanager::compile(1);
    &ui_print_footer( "edit_domain.cgi?dId=$in{dId}", 
                      $text{'edit_domain_title'} );
} 

