#!/usr/bin/perl


require "seam-lib.pl";
&ReadParse();



my $user = get_user_by_id( $in{uId} );

$desc = &text( "edit_user_desc", $user->{username} );
&ui_print_header( $desc, $text{'edit_user_title'}, undef );
                                                                                

#--------------------------- ALIAS MANAGEMENT ---------------------------------

print &ui_subheading($text{'edit_user_aliases'});

@table_links = ( &select_all_link("aId", 0),
                 &select_invert_link("aId", 0),                                 
                 &ui_link("add_alias.cgi?uId=$in{uId}", 
                          $text{'edit_user_add_alias'}) );

@col_attrs = ("width=5");                                                       
                                                                                
# Render a form for selecting a domain which submddits to select_user.cgi       
print &ui_form_start( "delete_alias.cgi" );                        
print &ui_links_row( \@table_links );                                           
print &ui_columns_start( ["", $text{'edit_user_alias_list'}], 50, 0, \@col_attrs );
                                                                                
@aliases = get_aliases( $user->{username} );                                                

foreach my $cur (@aliases) {                                                      
                                                                                
    local @cols = ("$cur->{destination}");
    #print $cur->{destination};
    print &ui_checked_columns_row(\@cols, \@col_attrs, "aId", $cur->{id});      
}                                                                               
                                                                                
print &ui_columns_end();                                                        
print &ui_links_row( \@table_links );                                           
print &ui_form_end( [[ "actionBtn", $text{'edit_user_delete_aliases'}]] );      
 

print &ui_hr();#------------------- PASSWORD MANAGEMENT --------------------------

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

                  
&ui_print_footer("edit_domain.cgi?dId=$user->{domain}", $text{'edit_domain_title'});
