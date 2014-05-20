#!/usr/bin/perl -w

require "seam-lib.pl";

my @domains = get_domains();

print qq~<select name="domain" id="domain">\n~;                                                                                                                                              

foreach my $entry (@domains) {
    print qq~\t<option value="$entry->{id}">$entry->{name}</option>\n~;   
}

print qq~</select>\n~;



