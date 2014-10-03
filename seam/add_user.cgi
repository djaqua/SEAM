#!/usr/bin/perl

use CGI;

require "seam-lib.pl";

ui_print_header( undef, $text{'add_user_title'}, "SEAM", undef, 1, 1 );

my $cgi = CGI->new();

my $domain = $cgi->param('domain_id');



