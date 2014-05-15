#!/usr/bin/perl

use DBI;
require 'seam-lib.pl';

                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );
print qq~<form action="update.cgi" method="post">~;

# Output a select field for a form which contains all the usernames for 
# a particular domain.
#print qq~<select name="username">~;
@usernames = (get_usernames());
foreach my $fields (@usernames) {
    print qq~username="$fields{'username'}"~;
    #print qq~<option value="$fields{'id'}">$fields{'username'}</option>~;
}
#print qq~</select>~;

print qq~                                                                       
    <br>                                                                        
    Please provide a new password here                                          
    <input type="password" name="password1" id="password1">                     
    <br>                                                                        
    Please confirm your password here                                           
    <input type="password" name="password2" id="password2">                     
    <br>                                                                        
    <input type="submit" name="proceedBtn" value="Proceed">                     
    </form>                                                                     

~;  
