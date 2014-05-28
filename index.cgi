#!/usr/bin/perl

require 'seam-forms-lib.pl';
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM");

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

seam_domain_select_form();
 
