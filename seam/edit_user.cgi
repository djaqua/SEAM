#!/usr/bin/perl

use CGI;

require "seam-lib.pl";

ui_print_header( undef, $text{'edit_user_title'}, "SEAM", undef, 1, 1 );

my $cgi = CGI->new();

my $user = $cgi->param('user_id');


if ("new" eq $user) {
    
    # TODO: render form for a user name with 'Proceed' button
    # TODO: Write SQL to create a new User
    # TODO: Submit to add_domain.cgi 
    print "TODO: Implement this use-case";

} elsif ("" ne $user) {


    # TODO print &ui_subheading($text{'edit_user_autoresponse'});
    # TODO print &ui_textarea("autoresponse", "", 4, 40);


    # TODO print &ui_subheading($text{'edit_user_forwards'});


    print &ui_subheading($text{'edit_user_password'});
    print qq~
        <p>Passwords must contain at least 8 mixed-case alphanumeric characters. 
        While the use of symbols (!@#\$%^&*?<>,.:;"'{+-}[_=]|) is not strictly 
        required, it is strongly encouraged.</p>

        <p>Examples of acceptable passwords include "Super123", "3v3nBetter", and 
        "b3\$tt0d\@t3"</p>
    ~;
    print &ui_password("password1");

    print &ui_password("password2");

}
