#!/usr/bin/perl 

=head seam-js-lib.pl
    
    Library for organizing the use of JavaScript throughout SEAM.

    require "pjsmanager.pl";

=cut
use strict;
package pjsmanager;

# source of all JavaScript managed by this module
my %functions = ();
my %statements = ();

#------------------------------------------------------------------------------

=head2 use_getObject()
    Adds JavaScript functionality for fetching a DOM object by its id 
    attribute. 

    Example invokation:
        pjsmanager::use_getObject();

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

#------------------------------------------------------------------------------

=head2 use_addExampleInputText()

    Controls the formatting and presentation of the example for a text
    field. When the specified text field has the focus, this function
    will clear the example and reset the formatting if the value of the 
    text field is exampleValue.  


    Example invokation:
    
        pjsmanager::use_addExampleInputText();
        print pjsmanager::compile();

    Results in the following JavaScript:
         
        function addExampleInputText(fieldId, exampleValue) {
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

        var originalColor = field.style.color;
        var exampleColor = "#A0A0A0";
        
        function exampleUpdate(textField) {
             
            if (exampleValue == textField.value) { 
                textField.value = "";
                textField.style.color = originalColor;

            } else if (!textField.value) { 
                textField.value = exampleValue;
                textField.style.color = exampleColor;
            } 
        }
        

        field.onblur = function() {
            exampleUpdate( this ); // 'this' refers to field
        };

        field.onfocus = function() {
            exampleUpdate( this ); // 'this' refers to field
        };
        
        exampleUpdate( field );
            
    }
    \n~;
}
#------------------------------------------------------------------------------

# TODO add text validation function ...

=head2 use_addValueChangeAutoSubmit()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
    pjsmanager::use_addValueChangeAutoSubmit();
    print pjsmanager::compile();

    Results in the following JavaScript:
         
        function addValueChangeAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }   

=cut
sub use_addValueChangeAutoSubmit {
    use_getObject();
    $functions{addValueChangeAutoSubmit}=qq~ 
    function addValueChangeAutoSubmit(sourceId, formId) {
        getObject( sourceId ).onchange = function() {
            getObject( formId ).submit();
        };
    }
    \n~;
}

#------------------------------------------------------------------------------
=head2 use_addValueChangeAutoClick()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        pjsmanager::use_addValueChangeAutoClick();
        print pjsmanager::compile();

    Results in the following JavaScript:
         
        function addValueChangeAutoClick(proxyId, subjectId) {
            ...
        }
        function getObject(domId) {
            ...
        }   

=cut
sub use_addValueChangeAutoClick {
    use_getObject();
    $functions{addValueChangeAutoClick}=qq~ 
    function addValueChangeAutoClick(proxyId, subjectId) {
        getObject( proxy ).onchange = function() {
            getObject( subject ).click();
        };
    }
    \n~;
}

#------------------------------------------------------------------------------


=head2 exampleInputText()

    Adds JavaScript functionality for automatic-form-submission. This function
    will automatically use getObject and its dependencies if they are not 
    already being used.

    Example invokation:
    
        pjsmanager::exampleInputText("emailField", "you@example.net");
        print pjsmanager::compile();

    Results in the following JavaScript:
         
        function addInputTextExample(fieldId, exampleValue) {
            ...
        }
        function getObject(domId) {
            ...
        }   
        addInputTextExample("emailField", "you@example.net");

=cut
sub exampleInputText {
    use_addExampleInputText();  # import the required library
    
    # improving readability
    my $field_id = $_[0];
    my $example_value = $_[1];

    $statements{'exampleInputText'} .= qq~
    addExampleInputText("$field_id", "$example_value");
    \n~;

}

#------------------------------------------------------------------------------

=head2 valueChangeAutoSubmit(source_id, form_id)

    Appends an invokation of 'autoSubmit' for the event-source and form 
    specified by source_id and form_id, respectively. This function will 
    automatically use addAutoSubmit and its dependencies if they are not 
    already being used. 
    
    Example invokation:

        pjsmanager::valueChangeAutoSubmit("domain", "domainSelectForm");
        pjsmanager::valueChangeAutoSubmit("user", "userSelectForm");
        print pjsmanager::compile();

    Results in the following JavaScript:
        
        addValueChangeAutoSubmit("domain", "domainSelectForm");
        addValueChangeAutoSubmit("user", "userSelectForm");
        function addValueChangeAutoSubmit(sourceId, formId) {
            ...
        }
        function getObject(domId) {
            ...
        }
=cut
sub valueChangeAutoSubmit {
    
    use_addValueChangeAutoSubmit();

    # improving readability
    my $source_id = $_[0];
    my $form_id = $_[1];

    $statements{'valueChangeAutoSubmit'} .= qq~
    addValueChangeAutoSubmit("$source_id", "$form_id");
    \n~;
}

#------------------------------------------------------------------------------
=head2 valueChangeAutoClick(proxy_id, subject_id)

    Appends an invokation of 'autoSubmit' for the event-source and form 
    specified by source_id and form_id, respectively. This function will 
    automatically use addAutoSubmit and its dependencies if they are not 
    already being used. 
    
    Example invokation:

        pjsmanager::valueChangeAutoClick("domainSelect", "updateDomainBtn");
        print pjsmanager::compile();

    Results in the following JavaScript:
        
        addValueChangeAutoClick("domainSelect", "updateDomainBtn");
        function addValueChangeAutoClick(proxyId, subjectId) {
            ... // see addValueChangeAutoClick
        }
        function getObject(domId) {
            ...
        }
=cut
sub valueChangeAutoClick {
    
    use_addValueChangeAutoClick();

    # improving readability
    my $proxy_id = $_[0];  
    my $subject_id = $_[1];

    # append the following JavaScript statement to the existing 'autoClick' 
    # string within the statements hash.

    $statements{'valueChangeAutoClick'} .= qq~
    addValueChangeAutoClick("$proxy_id", "$subject_id");
    \n~;
}


#------------------------------------------------------------------------------

=head2 compile(include_headers) 
    Returns a string representing the entire collection of scriptlets 
    configured through jsmanager. 

    If anything but 0 (zero) is specified for include_headers, then the opening and closing 'script' tags are included in the output. Otherwise, only the JavaScript is returned. 

    Example invokations:
        
        print jsmanager::compile(1);

        OR

        print jsmanager::compile();

    Results in the following JavaScript:
        <script type="text/javascript">

        </script>

        OR

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
   

sub clear {
    %functions = ();
    %statements = ();
}


1; # module requirement
