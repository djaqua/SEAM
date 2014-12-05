#!/usr/bin/perl

use CGI;

require "seam-lib.pl";


my $cgi = CGI->new();

my $domainId = $cgi->param('dId');
my $userName = $cgi->param('userName');
$actionBtn = $cgi->param('actionBtn');

if ($text{'proceed'} eq $actionBtn) {
   
    # TODO sanitize destination address 
    # TODO add forwarding address 
    $user = add_user( $userName, $domainId, "" );
    
    redirect("edit_user.cgi?uId=$user->{id}");
     
} elsif ($text{'cancel'} eq $actionBtn) {
    
    redirect("index.cgi");

} elsif ("" eq $actionBtn) {

    ui_print_header( undef, $text{'add_user_title'}, "SEAM", undef, 1, 1 );
    
    print &ui_form_start("add_user.cgi");

    print &ui_hidden("dId", $domainId);
    print &ui_textbox("userName");
    # TODO: autoexample with pjsmanager 

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    &ui_print_footer("edit_domain.cgi?dId=$domainId", $text{'add_user_return'});
} 

