#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: "EditDomain" 

use CGI;
                                          
require 'seam-lib.pl';

my $cgi = CGI->new();

my $domain = $cgi->param('domain_id');

@table_links = ( &select_all_link("user_id", 0), 
                 &select_invert_link("user_id", 0),
                 &ui_link("edit_user.cgi?user_id=new", $text{'users_add'}) );

@col_attrs = ("width=5");
                                                                               
ui_print_header( undef, $text{'edit_domain_title'}, "SEAM", undef, 1, 1 );



# Render a form for selecting a domain which submddits to select_user.cgi
print &ui_form_start( "delete_user.cgi" );
print &ui_links_row( \@table_links );
print &ui_columns_start( ["", 
                          $text{'users_username'}, 
                          $text{'users_autoresponse'}, 
                          $text{'users_forwards'}], 50, 0, \@col_attrs );

@users = get_users( $domain );    
foreach my $cur (@users) {
    
    local @cols = ("<a href='edit_user.cgi?user_id=$cur->{id}'>$cur->{username}</a>",
                   "",  # TODO query autoresponse details; dates/active etc
                   ""); # TODO query forwarding addresses for current user 
    print &ui_checked_columns_row(\@cols, \@col_attrs, "user_id", $cur->{id});
}


print &ui_columns_end();
print &ui_links_row( \@table_links );
print &ui_form_end( [[ "actionBtn", $text{'users_delete'}]] );

&ui_print_footer("", $text{'edit_domain_return'});
