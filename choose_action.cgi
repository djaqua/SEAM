#!/usr/bin/perl


use CGI;
require 'seam-forms-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
my $user =$cgi->param('user');
                                                                              
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );
print qq~
<script type="text/javascript">
function getObject(domId) {                                                     
    if (document.getElementById) {                                              
        return document.getElementById(domId);                                  
    } else if (document.all) {                                                  
        return document.all[domId];                                             
    } else if (document.layers) {                                               
        return document.layers[domId];                                          
    }                                                                           
}
</script>
~;

seam_domain_select_form( undef, undef, $domain );

seam_user_select_form( $domain, undef, undef, $user );

#print qq~<form id="userSelectForm" action="choose_action.cgi" method="POST">~;
#print qq~<input type="hidden" name="domain" value="$domain">~;
#seam_user_selector( $domain, $user );
#    <form>
print qq~
    CHOOSE ACTION
    <form action="add_forwarder.cgi" method="POST">
        
        <input type="hidden" name="user" value="$user">
        <input type="hidden" name="domain" value="$domain">
        <input type="text" name="destination" id="destination">
        <input type="submit" name="addForwarderBtn" value="Add Forwarder">
    </form>

    <form action="update_password.cgi" method="POST">
        
        <input type="hidden" name="user" value="$user">

        Please provide a new password here                  
        <input type="password" name="password1" id="password1">          
        <br>                                                              
        Please confirm the new password here                  
        <input type="password" name="password2" id="password2">
        <br>                                                
        <input type="submit" name="updatePasswordBtn" value="Update Password">
    
    </form>    
~;  
