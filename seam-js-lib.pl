#!/usr/bin/perl 

use strict;

package seam_js;


my %scriptlets = ();


=head2 init_seam_js()

=cut
sub use_getObject {
    
    $scriptlets{getObject}=qq~ 
    function getObject(domId) {
        if (document.getElementById) {
            return document.getElementById(domId);
        } else if (document.all) {
            return document.all[domId];
        } else if (document.layers) {
            return document.layers[domId];
        }
    }
    \n~;
}

sub use_addAutoSubmit {
    use_getObject();
    $scriptlets{addAutoSubmit}=qq~ 
    function addAutoSubmit(sourceId, formId) {
        getObject(sourceId).onchange = function() {
            getObject(formId).submit();
        }
    }
    \n~;
}

sub autoSubmit {
    use_addAutoSubmit();
    my $source_id = $_[0];
    my $form_id = $_[1];

    $scriptlets{'autoSubmit'} .= qq~
    addAutoSubmit("$source_id", "$form_id");
    \n~;
}

sub compile {

    my $javascript;

    foreach my $key (keys %scriptlets) {
        $javascript .= $scriptlets{$key}
    }

    return qq~<script type="text/javascript">$javascript</script>~;
}   



return 1;
