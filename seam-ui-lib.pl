#!/usr/bin/perl -w
=head1 seam-ui-lib.pl
 
 Functions for managing the Simple Email Administration Module

=cut

require "seam-lib.pl";

=head2 get_param(argument, default_value)
=cut
sub get_param {
    return (defined $_[0] and $_[0] ne "") ? $_[0] : defined $_[1] ? $_[1] : "";
}


=head2 seam_domain_selector(default_domain_id, form_field_id) 

    Renders a form select-field which allows the for selection of ONE from a 
    list of all virtual domains. If a default virtual domain is specified, then
    it is rendered as being selected by default, otherwise, [TODO]. If a form
    field id is specified, the form select-field is rendered with both a name
    and id equal to the specified field-id, otherwise, the default DOM
=cut
sub seam_domain_selector {

    # improve readability, unify format 
    local $default_domain_id = (defined $_[0] and "" ne $_[0]) ? $_[0] : "";
    local $form_field_id = (defined $_[1] and "" ne $_[1]) ? $_[1] : "domain";
    
    local @domains = get_domains();

    my $str_value = qq~<select name="$form_field_id" id="$form_field_id">\n~;

    
    foreach my $entry (@domains) {

        $str_value .= qq~\t<option value="$entry->{id}"~;
        
        if ($default_domain_id eq $entry->{id}) {
            $str_value .= qq~ selected~;
        }
        
        $str_value .= qq~>$entry->{name}</option>\n~;   
    }

    $str_value .= qq~</select>\n~;
    return $str_value;
}

=head2 seam_user_selector(domain_id, default_user_id, form_field_id) 

    Renders a form select-field for that allows the selection of ONE from a 
    list of all the users for a virtual domain specified by domain_id.
=cut
sub seam_user_selector {
 
    # improve readability, unify format
    local $domain = get_param( $_[0] );    
    local $default_user = get_param( $_[1] );
    local $field_id = get_param( $_[2], "user" );
 
    local $str_value = qq~<select name="$field_id" id="$field_id">\n~;                                                                                                                                              
    
    if ("" ne $domain) {
        local @users = get_users( $domain );
        foreach my $entry (@users) {
            $str_value .= qq~ <option value="$entry->{id}"~;
            if ($entry->{id} eq $default_user) {
                $str_value .= " selected";
            }
            $str_value .= qq~>$entry->{username}</option>\n~;   
        }
    }
    
    $str_value .= qq~</select>\n~;
    return $str_value;
}

