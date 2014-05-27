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

print qq~<form id="userSelectForm" action="choose_action.cgi" method="POST">
<input type="hidden" name="domain" value="$domain">~;

seam_user_selector( $domain );
print qq~
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

getObject("user").onchange = function() {
    getObject("userSelectForm").submit();
};
</script>
~;  
