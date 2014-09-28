#!/usr/bin/perl

use CGI;
require 'seam-lib.pl';

my $cgi = CGI->new();

if (defined $cgi->param('action')) {

    my $action = $cgi->param('action');
    
    if ("Update Password" eq $action) {
        
        redirect('update_password.cgi');        

    } elsif ("Add Forwarder" eq $action) {
        
        redirect('add_forwarder.cgi');        

    } elsif ("Add Autoresponder" eq $action) {

        redirect('add_autoresponder.cgi');        
    
    } else {

        redirect('choose_action.cgi');        
    }
}

 


