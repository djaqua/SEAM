#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: 

require 'seam-forms-lib.pl';
require 'seam-js-lib.pl';

                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM");

# Render a form for selecting a domain which submits to select_user.cgi
print seam_domain_select_form();

# Include javascript functionality
print seam_js::compile(1); 
