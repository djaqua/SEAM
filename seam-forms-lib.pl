#!/usr/bin/perl -w

require "seam-ui-lib.pl";
require "seam-js-lib.pl";

=head2 seam_domain_select_form(form_action, form_id, default_domain)
=cut
sub seam_domain_select_form {

    local $form_action = get_param( $_[0], "select_user.cgi" );
    local $form_id = get_param( $_[1], "domainSelectForm" );
    local $default_domain = get_param( $_[2] );
    local $domain_field_id = get_param( $_[3], "domain" );
    
    seam_js::autoSubmit( $domain_field_id, $form_id );

    local $str_value;
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");

    # its okay if $default_domain_id is the empty string or undefined
    $str_value .= seam_domain_selector( $default_domain, $domain_field_id );
        
    #$str_value .= qq~ 
    #<script type="text/javascript"> 
    #getObject("$domain_field_id").onchange = function() {
    #    getObject("$form_id").submit();
    #};
    #</script>~;

    $str_value .= qq~<input type="submit" value="Update Domain">~;


    $str_value .= ui_form_end();
    return $str_value;
}

=head2 seam_domain_select_form(domain, form_action, form_id, default_user, user_field_id)
    
=cut
sub seam_user_select_form {

    local $domain = get_param( $_[0] );
    local $form_action = get_param( $_[1], "choose_action.cgi" );
    local $form_id = get_param( $_[2], "userSelectForm" );
    local $default_user = get_param( $_[3] );
    local $user_field_id = get_param( $_[4], "user" );

    seam_js::autoSubmit( $user_field_id, $form_id );
    
    local $str_value;                                                   
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");
    $str_value .= seam_user_selector( $domain, $default_user );                                                  
    $str_value .= qq~                                                                       
    <input type="hidden" name="domain" value="$domain">
    <input type="submit" value="Update User">
    ~;
    $str_value .= ui_form_end();

    return $str_value;

}

sub seam_add_forwarder_form {

    local $user = get_param( $_[0] );
    local $domain = get_param( $_[1] );
    local $form_action = get_param( $_[2], "add_forwarder.cgi" );
    local $form_id = get_param( $_[3], "addForwarderForm" );

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


