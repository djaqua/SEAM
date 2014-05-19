#!/usr/bin/perl

use DBI;
require 'seam-lib.pl';

                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );
print qq~<form action="update.cgi" method="post">~;

my $stmt = get_database()->prepare( $select_users );                        
$stmt->execute or die qq~                                                  
    Simple Email Administration Modules says:                              
    "Whoops, $DBI::errstr"                                                 
~;

# Output a select field for a form which contains all the usernames for 
# a particular domain.
my @users = get_users(25);
print qq~<select name="user">~;                                                                                                                                              
#while (@fields = $stmt->fetchrow_array) {                                  
#    print qq~<option value="$fields[0]">$fields[1]</option>~;
#}
foreach my $entry (@users) {

    print qq~ <option value="$entry->{id}">$entry->{username}</option>~;   
}
print qq~</select>~;
                                                                            
$stmt->finish();                                                           
get_database()->disconnect();   


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
