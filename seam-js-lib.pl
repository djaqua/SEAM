#!/usr/bin/perl 
=head seam-js-lib.pl
    
    Library for organizing the use of JavaScript throughout SEAM.

    require "seam-js-lib.pl";

=cut
use strict;
package seam_js;

# source of all JavaScript managed by this module
my %functions = ();
my %statements = ();


=head2 use_getObject()
    Adds JavaScript functionality for fetching a DOM object by its id 
    attribute. 

    Example invokation:
        seam_js::use_getObject();

    Results in the following JavaScript:
        function getObject(domId) { 
            ...
        }

=cut
sub use_getObject {
    
    $functions{getObject}=qq~ 
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

=head2 use_addExampleInputText()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        seam_js::use_addInputTextExample();
        print seam_js::compile();

    Results in the following JavaScript:
         
        function addAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }   

=cut
sub use_addExampleInputText {
    use_getObject();
    $functions{addExampleInputText}=qq~ 
    function addExampleInputText(fieldId, exampleValue) {

        field = getObject( fieldId );
        field.onblur = function() {
            if ( !this.value ) {
                this.value = exampleValue;
                this.style.color = "#A0A0A0";
            }
        };
        field.onfocus = function() {
            if (exampleValue == this.value) {
                this.value = "";
                this.style.color = "#000000";
            }
        };
    }
    \n~;
}


=head2 use_addAutoSubmit()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        seam_js::use_addAutoSubmit();
        print seam_js::compile();

    Results in the following JavaScript:
         
        function addAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }   

=cut
sub use_addAutoSubmit {
    use_getObject();
    $functions{addAutoSubmit}=qq~ 
    function addAutoSubmit(sourceId, formId) {
        getObject( sourceId ).onchange = function() {
            getObject( formId ).submit();
        };
    }
    \n~;
}

=head2 use_addAutoClick()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        seam_js::use_addAutoSubmit();
        print seam_js::compile();

    Results in the following JavaScript:
         
        function addAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }   

=cut
sub use_addAutoClick {
    use_getObject();
    $functions{addAutoClick}=qq~ 
    function addAutoClick(sourceId, proxyBtn) {
        getObject(sourceId).onchange = function() {
            getObject(proxyBtn).click();
        };
    }
    \n~;
}



=head2 exampleInputText()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        seam_js::exampleInputText("emailField", "you@example.net");
        print seam_js::compile();

    Results in the following JavaScript:
         
        function addInputTextExample(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }   
        addInputTextExample(source

=cut
sub exampleInputText {
    use_addExampleInputText();  # import the required library
    
    my $field_id = $_[0];
    my $example_value = $_[1];

    $statements{'exampleInputText'} .= qq~
    addExampleInputText("$field_id", "$example_value");
    \n~;

}


=head2 autoSubmit(source_id, form_id)

    Appends an invokation of 'autoSubmit' for the event-source and form 
    specified by source_id and form_id, respectively. This function will 
    automatically use addAutoSubmit and its dependencies if they are not 
    already being used. 
    
    Example invokation:

        seam_js::autoSubmit("domain", "domainSelectForm");
        seam_js::autoSubmit("user", "userSelectForm");
        print seam_js::compile();

    Results in the following JavaScript:
        
        addAutoSubmit("domain", "domainSelectForm");
        addAutoSubmit("user", "userSelectForm");
        function addAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }
=cut
sub autoSubmit {
    
    use_addAutoSubmit();

    my $source_id = $_[0];
    my $form_id = $_[1];

    $statements{'autoSubmit'} .= qq~
    addAutoSubmit("$source_id", "$form_id");
    \n~;
}

sub autoClick {
    
    use_addAutoClick();

    my $source_id = $_[0];
    my $proxy_id = $_[1];

    $statements{'autoClick'} .= qq~
    addAutoClick("$source_id", "$proxy_id");
    \n~;
}



=head2 compile(include_headers) 
    Returns a string representing the entirety of scriptlets enclosed between
    script open and close tags if anything but 0 (zero) is specified for 
    include_headers, otherwise, only the JavaScript is returned. 

    Example invokations:
        
        print seam_js::compile(1);

    Results in the following JavaScript:
        <script type="text/javascript">

        </script>
=cut
sub compile {
    my $javascript;
    foreach my $key (keys %functions) {
        $javascript .= $functions{$key}
    }

    foreach my $key (keys %statements) {
        $javascript .= $statements{$key}
    }
    if (defined $_[0]) {
        #headers
        return qq~<script type="text/javascript">\n$javascript\n</script>~;
    } else {
        # no headers
        return "$javascript\n";
    }
}  
 



1; # module requirement
