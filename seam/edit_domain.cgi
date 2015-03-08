#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: "EditDomain" 

require 'seam-lib.pl';

&ReadParse();

@table_links = ( &select_all_link("uId", 0), 
                 &select_invert_link("uId", 0),
                 &ui_link("add_user.cgi?dId=$in{dId}", 
                          $text{'edit_domain_add_user'}) );

@col_attrs = ("width=5");
 
my $domain = get_domain_by_id( $in{dId} );
my $desc = &text( "edit_domain_desc", $domain->{name} );                                                                               
&ui_print_header( $desc, $text{'edit_domain_title'}, undef);

# Render a form for selecting a domain which submddits to select_user.cgi
print &ui_form_start( "delete_user.cgi" );
print &ui_links_row( \@table_links );
print &ui_columns_start( ["", 
                          $text{'edit_domain_user_list_username'}, 
                          $text{'edit_domain_user_list_autoresponse'}, 
                          $text{'edit_domain_user_list_alias'}], 
                         50, 0, \@col_attrs );

@users = get_users( $in{dId} );    
foreach my $cur (@users) {
 
    local $alias_str = "";
    local @aliases = get_aliases( $cur->{username} );
    for my $alias (@aliases) {
        $alias_str .= $alias->{destination} . ", ";
    }
    $alias_str = substr( $alias_str, 0, length($alias_str)-2 );
   
    local @cols = ("<a href='edit_user.cgi?uId=$cur->{id}'>$cur->{username}</a>",
                   "",  # TODO query autoresponse details; dates/active etc
                   $alias_str );
    print &ui_checked_columns_row(\@cols, \@col_attrs, "uId", $cur->{id});
}


print &ui_columns_end();
print &ui_links_row( \@table_links );
print &ui_form_end( [[ "actionBtn", $text{'edit_domain_delete_users'}]] );

&ui_print_footer("index.cgi", $text{'edit_mailserver_title'});
