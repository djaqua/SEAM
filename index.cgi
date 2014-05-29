#!/usr/bin/perl

require 'seam-forms-lib.pl';
require 'seam-js-lib.pl';
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM");

print seam_js_getObject();


print seam_domain_select_form();
 
