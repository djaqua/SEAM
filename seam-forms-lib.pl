#!/usr/bin/perl -w

require "seam-ui-lib.pl";

=head2 seam_domain_select_form(form_action, form_id, default_domain)
=cut
sub seam_domain_select_form {

    local $form_action = get_param( $_[0], "select_user.cgi" );
    local $form_id = get_param( $_[1], "domainSelectForm" );
    local $default_domain = get_param( $_[2] );
    local $domain_field_id = get_param( $_[3], "domain" );

    local $str_value;
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");

    # its okay if $default_domain_id is the empty string or undefined
    $str_value .= seam_domain_selector( $default_domain, $domain_field_id );
        
    $str_value .= qq~ 
    <script type="text/javascript"> 
    getObject("$domain_field_id").onchange = function() {
        getObject("$form_id").submit();
    };
    </script>
    <input type="submit" value="Update Domain">
    ~;
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

    local $str_value;                                                   
    $str_value .= ui_form_start($form_action, "POST", undef, "id=\"$form_id\"");
                                                                                
    $str_value .= seam_user_selector( $domain, $default_user );                                                  

    $str_value .= qq~                                                                       
    <input type="hidden" name="domain" value="$domain">
    <script type="text/javascript">                                               
                                                                                    
    getObject("$user_field_id").onchange = function() {                                     
        getObject("$form_id").submit();                                       
    };                                                                            
                                                                                    
    </script>                                                                     
    <input type="submit" value="Update User">
    ~;   

    $str_value .= ui_form_end();

    return $str_value;

}
