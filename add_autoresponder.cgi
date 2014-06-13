#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

print ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
 

my $cgi = CGI->new();



local $source_domain = $cgi->param('domain'); 

local $selected_user_id = $cgi->param('user');


local $message_body = $cgi->param('messageText');



get_database()->disconnect();
print ui_print_footer( "", $text{'index_return'},);

 


