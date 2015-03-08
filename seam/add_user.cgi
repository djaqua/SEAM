#!/usr/bin/perl

use CGI;

require "seam-lib.pl";
require "pjsmanager.pl";

my $cgi = CGI->new();

my $domainId = $cgi->param('dId');
my $userName = $cgi->param('userName');
$actionBtn = $cgi->param('actionBtn');

if ($text{'proceed'} eq $actionBtn) {
    
    # TODO sanitize $domainName
   
    $user = add_user( $userName, $domainId, "" );
    
    redirect("edit_user.cgi?uId=$user->{id}");
     
} elsif ($text{'cancel'} eq $actionBtn) {
    
    redirect("index.cgi");

} elsif ("" eq $actionBtn) {
    
    local $domainName = get_domain_by_id( $domainId )->{'name'};

    local $desc = &text( 'add_user_desc', $domainName );
    &ui_print_header( $desc, $text{'add_user_title'}, undef );
    
    print &ui_form_start("add_user.cgi");

    print &ui_hidden("dId", $domainId);
    
    print &ui_textbox("userName", undef, 32, 0, 32, 'id="userName"' );
    
    pjsmanager::exampleInputText("userName", "user\@$domainName");          

    print &ui_form_end( [[ "actionBtn", $text{'proceed'}], 
                         [ "actionBtn", $text{'cancel'}]] );

    print pjsmanager::compile(1);
    &ui_print_footer( "edit_domain.cgi?dId=$domainId", 
                      $text{'edit_domain_title'} );
} 

