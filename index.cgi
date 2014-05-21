#!/usr/bin/perl

require 'seam-lib.pl';
require 'seam-ui-lib.pl';
                                                                               
ui_print_header( undef, $text{'index_title'}, "");

print qq~<form id="domainSelectForm" action="select_user.cgi" action="POST">~;
seam_domain_selector();
print qq~</form>~;

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

    getObject("domain").onchange = function() {
        getObject("domainSelectForm").submit();
    };

    </script>
~;  
