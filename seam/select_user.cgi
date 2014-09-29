#!/usr/bin/perl

# Filename: select_user.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: 
use CGI;

require 'seam-forms-lib.pl';
require 'pjsmanager.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
                                                                               
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );

# Add JavaScript functionality for getting DOM objects by their id attribute



# Render a form for selecting a domain which submits to select_user.cgi (this)
print seam_domain_select_form( undef, undef, $domain );

# Renders a form for selecting a user which submits to choose_action.cgi
print seam_user_select_form( $domain );


# Include javascript functionality (with headers) for 
# the domain-select and user-select forms
print pjsmanager::compile( 1 );