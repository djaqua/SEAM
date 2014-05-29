#!/usr/bin/perl


use CGI;
require 'seam-forms-lib.pl';
require 'seam-js-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain');
my $user =$cgi->param('user');
                                                                              
ui_print_header( undef, $text{'index_title'}, "SEAM", undef, 1, 1 );

# Render a form for selecting a domain which submits to select_user.cgi
print seam_domain_select_form( undef, undef, $domain );

# Render a form for selecting a user which submits to choose_action.cgi (this)
print seam_user_select_form( $domain, undef, undef, $user );

# Render a form for adding a forwarder/alias which submits to add_forwarder.cgi
print seam_add_forwarder_form( $user, $domain );

# Render a form for changing a password which submits to update_password.cgi
print seam_update_password_form( $user );

# Include javascript functionality
print seam_js::compile();
