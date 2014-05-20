#!/usr/bin/perl

require 'seam-lib.pl';
require 'seam-ui-lib.pl';
                                                                               
ui_print_header( undef, $text{'index_title'}, "");

print qq~<form id="domainSelectForm" action="select_user.cgi" action="POST">~;
seam_domain_selector();
print qq~</form>~;

print qq~
<form action="update_password.cgi" action="post">
<select name="user">
~;

# Output a select field for a form which contains all the usernames for 
# a particular domain.
my @users = get_users(25);
foreach my $entry (@users) {
    print qq~ <option value="$entry->{id}">$entry->{username}</option>~;   
}

print qq~
    </select>                                                          
    <br>                                                                        
    Please provide a new password here                                          
    <input type="password" name="password1" id="password1">                     
    <br>                                                                        
    Please confirm your password here                                           
    <input type="password" name="password2" id="password2">                     
    <br>                                                                        
    <input type="submit" name="proceedBtn" value="Proceed">                     
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
