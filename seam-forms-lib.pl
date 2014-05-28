#!/usr/bin/perl -w

require "seam-ui-lib.pl";

=head2 seam_domain_select_form(form_action, form_id, default_domain)
=cut
sub seam_domain_select_form {

    local $form_action = get_param( $_[0], "select_user.cgi" );
    local $form_id = get_param( $_[1], "domainSelectForm" );
    local $default_domain = get_param( $_[2] );
    local $domain_field_id = get_param( $_[3], "domain" );
    
    print qq~ <form id="$form_id" action="$form_action" method="POST"> ~;

    # its okay if $default_domain_id is the empty string or undefined
    seam_domain_selector( $default_domain, $domain_field_id );
    
    print qq~ 
\t<script type="text/javascript"> 
\tgetObject("$domain_field_id").onchange = function() {
\t    getObject("$form_id").submit();
\t};
\t</script>
\t<input type="submit" value="Update Domain">
</form>
    ~;
}

=head2 seam_domain_select_form(domain, form_action, form_id, default_user, user_field_id)
    
=cut
sub seam_user_select_form {

    local $domain = get_param( $_[0] );
    local $form_action = get_param( $_[1], "choose_action.cgi" );
    local $form_id = get_param( $_[2], "userSelectForm" );
    local $default_user = get_param( $_[3] );
    local $user_field_id = get_param( $_[4], "user" );
                                                   
    print qq~ <form id="$form_id" action="$form_action" method="POST"> ~;            
                                                                                
    seam_user_selector( $domain, $default_user );                                                  

    print qq~                                                                       
\t<input type="hidden" name="domain" value="$domain">
\t<script type="text/javascript">                                               
                                                                                
\tgetObject("$user_field_id").onchange = function() {                                     
\t\tgetObject("$form_id").submit();                                       
\t};                                                                            
                                                                                
\t</script>                                                                     
\t<input type="submit" value="Update User">                  
</form>                                                                         
    ~;   

}
