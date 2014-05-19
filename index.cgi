#!/usr/bin/perl

require 'seam-lib.pl';
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );
print qq~<form action="update.cgi" method="post">~;

# Output a select field for a form which contains all the usernames for 
# a particular domain.
my @users = get_users(25);
print qq~<select name="user">~;                                                                                                                                              
foreach my $entry (@users) {
    print qq~ <option value="$entry->{id}">$entry->{username}</option>~;   
}
print qq~</select>~;

# Render the rest of the update-password-form.                                                                            
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
