#!/usr/bin/perl

require "seam-lib.pl";

ui_print_header( undef, $text{'edit_domain_title'}, "SEAM", undef, 1, 1 );

print &ui_textarea("autoresponse", "", 4, 40);

