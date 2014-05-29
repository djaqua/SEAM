#!/usr/bin/perl 

=head2 init_seam_js()

=cut
sub seam_js_getObject {
    
    return qq~
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
}


return 1;
