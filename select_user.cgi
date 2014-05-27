#!/usr/bin/perl

use CGI;
require 'seam-lib.pl';
require 'seam-ui-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
if (undef == $domain) {
    print "undefined!";
}
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );
print qq~
~;

print qq~<form id="domainSelectForm" action="select_user.cgi" method="POST">~;
seam_domain_selector( $domain ); 
print qq~<input type="submit" value="Proceed">~;
print qq~</form>~;

print qq~<form action="edit_user.cgi" method="POST">~;
seam_user_selector( $domain );
print qq~

    <div style="border: 1px dashed #6395ED" id="addForwarderFields">                                                              
        <input type="hidden" name="domain" value="$domain">
        <input type="text" name="destination" id="destination">
        <input type="submit" name="addForwarderBtn" value="Add Forwarder">
    </div> 
    <div style="border: 1px dashed #6395ED" id="updatePasswordFields"> 
        Please provide a new password here                  
        <input type="password" name="password1" id="password1">          
        <br>                                                              
        Please confirm your password here                  
        <input type="password" name="password2" id="password2">
        <br>                                                
        <input type="submit" name="updatePasswordBtn" value="Update Password">
    </div>
</form>       
     
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

getObject("domain").onchange = function() {
    getObject("domainSelectForm").submit();
};
</script>
~;  
