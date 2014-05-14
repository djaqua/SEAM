#!/usr/bin/perl

use DBI;
require 'seam-lib.pl';

$DBNAME="";
$DBUSER="";
$DBPASS="";

# TODO come back and use built-in module configuration capabilities             
# (/etc/webmin/seam/config)                                                     
#                                                                               
open(CONF, '/root/seam.conf');                                                  
while (<CONF>) {                                                                
                                                                                
    chomp;                                                                      
    my @line = split('=', $_);                                                  
                                                                                
    if ("username" eq $line[0]) {                                               
        $DBUSER = $line[1];                                                     
    } elsif ("password" eq $line[0]) {                                          
        $DBPASS = $line[1];                                                     
    } elsif ("database" eq $line[0]) {                                          
        $DBNAME = $line[1];                                                     
    }                                                                           
                                                                                
}                                                                               
close(CONF);  

ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );

$database = DBI->connect( "DBI:mysql:$DBNAME", $DBUSER, $DBPASS );
$user_query = "SELECT id, username FROM virtual_users WHERE domain=2";

$stmt = $database->prepare( $user_query );
$stmt->execute or die qq~
    Simple Email Administration Modules says:
    "Whoops, $DBI::errstr"
~;


print qq~<select name="username">~;
while (@fields_array = $stmt->fetchrow_array) {
    print qq~<option value="$fields_array[0]">$fields_array[1]</option>~;
}
print qq~</select>~;
$stmt->finish();
$database->disconnect();

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
