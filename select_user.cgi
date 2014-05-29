#!/usr/bin/perl

use CGI;
require 'seam-forms-lib.pl';
require 'seam-js-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );

print seam_js_getObject();

print seam_domain_select_form( undef, undef, $domain );

print seam_user_select_form( $domain );

