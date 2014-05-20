#!/usr/bin/perl -w

require "seam-lib.pl";


print qq~<select name="user" id="user">\n~;                                                                                                                                              

# Output a select field for a form which contains all the usernames for 
# a particular domain.

my @users = get_users( $domain );
foreach my $entry (@users) {
    print qq~ <option value="$entry->{id}">$entry->{username}</option>~;   
}

print qq~</select>\n~;



