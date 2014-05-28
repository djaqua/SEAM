#!/usr/bin/perl

use CGI;
require 'seam-forms-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
                                                                               
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


seam_user_select_form( $domain );

