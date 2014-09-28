#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: 

require 'seam-forms-lib.pl';
require 'pjsmanager.pl';

                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM" );

# Render a form for selecting a domain which submits to select_user.cgi
print seam_domain_select_form();

# Include javascript functionality (with headers) for the domain-select form
print pjsmanager::compile( 1 ); 

pjsmanager::clear();

