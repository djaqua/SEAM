#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: "EditDomain" 

use CGI;
                                          
require 'seam-lib.pl';

my $cgi = CGI->new();

my $domainId = $cgi->param('dId');

@table_links = ( &select_all_link("uId", 0), 
                 &select_invert_link("uId", 0),
                 &ui_link("add_user.cgi?dId=$domainId", 
                          $text{'edit_domain_add_user'}) );

@col_attrs = ("width=5");
                                                                               
ui_print_header( undef, $text{'edit_domain_title'}, "SEAM", undef, 1, 1 );

# Render a form for selecting a domain which submddits to select_user.cgi
print &ui_form_start( "delete_user.cgi" );
print &ui_links_row( \@table_links );
print &ui_columns_start( ["", 
                          $text{'edit_domain_user_list_username'}, 
                          $text{'edit_domain_user_list_autoresponse'}, 
                          $text{'edit_domain_user_list_alias'}], 
                         50, 0, \@col_attrs );

@users = get_users( $domainId );    
foreach my $cur (@users) {
    
    local @cols = ("<a href='edit_user.cgi?uId=$cur->{id}'>$cur->{username}</a>",
                   "",  # TODO query autoresponse details; dates/active etc
                   ""); # TODO query forwarding addresses for current user 
    print &ui_checked_columns_row(\@cols, \@col_attrs, "uId", $cur->{id});
}


print &ui_columns_end();
print &ui_links_row( \@table_links );
print &ui_form_end( [[ "actionBtn", $text{'edit_domain_delete_users'}]] );

&ui_print_footer("index.cgi", $text{'edit_mailserver_title'});
