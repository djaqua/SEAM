#!/usr/bin/perl -w

=head1 seam-ui-lib.pl

 Functions for managing the Simple Email Administration Module

=cut

require "seam-lib.pl";

=head2 seam_domain_selector() 

=cut
sub seam_domain_selector {
    local @domains = get_domains();

    print qq~<select name="domain" id="domain">\n~;                                                                                                                                              

    foreach my $entry (@domains) {
        if ($_[0] eq $entry->{id}) {
            print qq~\t<option value="$entry->{id}" selected>$entry->{name}</option>\n~;   
        } else {
            print qq~\t<option value="$entry->{id}">$entry->{name}</option>\n~;   
        }
    }

    print qq~</select>\n~;
}

=head2 seam_user_selector(domain_id) 

=cut
sub seam_user_selector {
     
    local @users = get_users( $_[0] );
    
    print qq~<select name="user" id="user">\n~;                                                                                                                                              
    
    foreach my $entry (@users) {
        print qq~ <option value="$entry->{id}">$entry->{username}</option>~;   
    }

    print qq~</select>\n~;
}
