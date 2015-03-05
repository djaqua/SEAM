#!/usr/bin/perl

use CGI;

require "seam-lib.pl";
&ReadParse();

ui_print_header( undef, $text{'edit_user_title'}, "SEAM", undef, 1, 1 );

my $cgi = CGI->new();

my $user = get_user_by_id( $in{uId} );



print &ui_subheading($text{'edit_user_password'});
print qq~
    <p>Passwords must contain at least 8 mixed-case alphanumeric characters. 
    While the use of symbols (!@#\$%^&*?<>,.:;"'{+-}[_=]|) is not strictly 
    required, it is strongly encouraged.</p>

    <p>Examples of acceptable passwords include "Super123", "3v3nBetter", and 
    "b3\$tt0d\@t3"</p>
~;
print &ui_form_start("update_password.cgi", "post");
print &ui_hidden("uId", $user->{id});
print "<p>Please provide a new password here: " . &ui_password("password1") . "</p>";

print "<p>Please confirm the password here: " . &ui_password("password2") . "</p>";
print &ui_form_end( [["actionBtn", $text{save}],
                     ["actionBtn", $text{cancel}]] );

print &ui_hr();#----------------------------------------------------------------
                                                                                
@table_links = ( &select_all_link("uId", 0),                                    
                 &select_invert_link("uId", 0),                                 
                 &ui_link("add_alias.cgi?uId=$in{uId}", 
                          $text{'edit_user_add_alias'}) );
                                                                                
@col_attrs = ("width=5");                                                       
                                                                                
                                                                                
# Render a form for selecting a domain which submddits to select_user.cgi       
print &ui_form_start( "delete_alias.cgi" );                        
print &ui_links_row( \@table_links );                                           
print &ui_columns_start( ["", $text{'edit_user_alias_list'}], 50, 0, \@col_attrs );   
                                                                                
$user = get_user_by_id( $in{uId} );                                             

@forwards = get_forwarding_addresses( $user->{username} );
                                                                                
#foreach my $cur (@users) {                                                     
                                                                                
#    local @cols = ("<a href='edit_user.cgi?uId=$cur->{id}'>$cur->{username}</a>",
#                   "",  # TODO query autoresponse details; dates/active etc    
#                   ""); # TODO query forwarding addresses for current user     
#    print &ui_checked_columns_row(\@cols, \@col_attrs, "uId", $cur->{id});     
#}                                                                              
                                                                                
                                                                                
print &ui_columns_end();                                                        
print &ui_links_row( \@table_links );                                           
print &ui_form_end( [[ "actionBtn", $text{'edit_user_delete_aliases'}]] );     



&ui_print_footer("edit_domain.cgi?dId=$user->{domain}", $text{'edit_domain_title'});
