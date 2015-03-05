#!/usr/bin/perl
use CGI;


use DBI;
require 'seam-lib.pl';

 

my $cgi = CGI->new();

my $actionBtn = $cgi->param('actionBtn');
my $user = get_user_by_id( $cgi->param('uId') );
my $password1 = $cgi->param('password1');
my $password2 = $cgi->param('password2');


if ($text{save} eq $actionBtn) {
    
    if ($password1 eq $password2) {
        update_password($user->{id}, $password1);
        redirect("edit_domain.cgi?dId=$user->{domain}");
    } else {

        ui_print_header( "", $text{'index_title'}, "SEAM", undef, 1, 1);
        # TODO PASSWORD MISMATCH
        ui_print_footer( "", $text{'index_return'},);

    }

} elsif ($text{cancel} eq $actionBtn) {
    redirect("edit_user.cgi?uId=$user->{id}");
}



 


