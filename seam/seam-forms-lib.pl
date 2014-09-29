#!/usr/bin/perl -w

require "seam-ui-lib.pl";
require "pjsmanager.pl";


sub seam_add_forwarder_form {

    local $user = get_param( $_[0] );
    local $domain = get_param( $_[1] );
    local $form_action = get_param( $_[2], "add_forwarder.cgi" );
    local $form_id = get_param( $_[3], "addForwarderForm" );

    pjsmanager::exampleInputText( "destination", 'user@somewhere.net' );

    local $str_value;
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");
        
    $str_value .= qq~
    <input type="hidden" name="user" value="$user">
    <input type="hidden" name="domain" value="$domain">
    <input type="text" name="destination" id="destination">
    <input type="submit" name="addForwarderBtn" value="Add Forwarder">
    ~;
    
    $str_value .= ui_form_end();

    return $str_value;
}
sub seam_update_password_form {

    local $user = get_param( $_[0] );
    local $form_action = get_param( $_[1], "update_password.cgi" );
    local $form_id = get_param( $_[2], "updatePasswordForm" );

    local $str_value;
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");

    $str_value .= qq~
    
    <input type="hidden" name="user" value="$user">

    Please provide a new password here                  
    <input type="password" name="password1" id="password1">          
    <br>                                                              
    Please confirm the new password here                  
    <input type="password" name="password2" id="password2">
    <br>                                                
    <input type="submit" name="updatePasswordBtn" value="Update Password">

    ~;
    
    $str_value .= ui_form_end();

    return $str_value;
}


