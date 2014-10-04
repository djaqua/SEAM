#!/usr/bin/perl

use CGI;

require "seam-lib.pl";

ui_print_header( undef, $text{'edit_user_title'}, "SEAM", undef, 1, 1 );

my $cgi = CGI->new();

my $user = get_user_by_id( $cgi->param('uId') );



print &ui_hr();
print &ui_subheading($text{'edit_user_autoresponse'});
# TODO print &ui_textarea("autoresponse", "", 4, 40);
include( "test" );


print &ui_hr();

print &ui_subheading($text{'edit_user_forwards'});

print &ui_hr();

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
print &ui_hr();

&ui_print_footer("edit_domain.cgi?dId=$user->{domain}", $text{'add_user_return'});
