#!/usr/bin/perl


# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: "EditServer" 

require 'seam-lib.pl';

#my $desc = &text( "edit_mailserver_desc",                                                                                
&ui_print_header( "", $text{'edit_mailserver_title'}, undef );

# Render a form for selecting a domain which submits to select_user.cgi

@table_links = ( &select_all_link("dId", 0), 
                &select_invert_link("dId", 0),
                &ui_link("add_domain.cgi", 
                         $text{'edit_mailserver_add_domain'}) );
@col_attrs = ("width=5");

print &ui_form_start( "delete_domain.cgi" );
print &ui_links_row( \@table_links );
print &ui_columns_start( ["",$text{'edit_mailserver_domain_list'}], 50, 0, \@col_attrs );

@domains = get_domains();    
foreach my $cur (@domains) {

    local @cols = ("<a href='edit_domain.cgi?dId=$cur->{id}'>$cur->{name}</a>");
    print &ui_checked_columns_row(\@cols, \@col_attrs, "dId", $cur->{id});
}



print &ui_columns_end();
print &ui_links_row( \@table_links );
print &ui_form_end( [[ "actionBtn", $text{'edit_mailserver_delete_domains'}]] );


&ui_print_footer("", $text{'edit_mailserver_return'});
