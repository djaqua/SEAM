#!/usr/bin/perl

# Filename: index.cgi
# Author: Drew Jaqua <djaqua@smnet.net>
# Description: "EditServer" 

require 'seam-lib.pl';

                                                                               
&ui_print_header( undef, $text{'edit_mailserver_title'}, "SEAM" );

# Render a form for selecting a domain which submits to select_user.cgi

@table_links = ( &select_all_link("domain_id", 0), 
                &select_invert_link("domain_id", 0),
                &ui_link("edit_domain.cgi?domain_id=new", $text{'domains_add'}) );
@col_attrs = ("width=5");

print &ui_form_start( "delete_domain.cgi" );
print &ui_links_row( \@table_links );
print &ui_columns_start( ["",$text{'domains_domain'}], 50, 0, \@col_attrs );

@domains = get_domains();    
foreach my $cur (@domains) {

    local @cols = ("<a href='edit_domain.cgi?domain_id=$cur->{id}'>$cur->{name}</a>");
    print &ui_checked_columns_row(\@cols, \@col_attrs, "domain_id", $cur->{id});
}



print &ui_columns_end();
print &ui_links_row( \@table_links );
print &ui_form_end( [[ "actionBtn", $text{'domains_delete'}]] );


&ui_print_footer("", $text{'edit_mailserver_return'});
