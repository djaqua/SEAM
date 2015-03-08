#!/usr/bin/perl


require 'seam-lib.pl';
&ReadParse();
 


my $user = get_user_by_id( $in{uId} );


if ($text{save} eq $in{actionBtn}) {
    
    if ($in{password1} eq $in{password2}) {
        update_password($user->{id}, $in{password1});
        redirect("edit_domain.cgi?dId=$user->{domain}");
    } else {

        &ui_print_header( undef, $text{'update_password_title'}, undef );
        # TODO PASSWORD MISMATCH
        print "TODO: functionality (warning and redraw form)";
        &ui_print_footer( "", $text{'index_return'},);

    }

} elsif ($text{cancel} eq $in{actionBtn}) {
    redirect("edit_user.cgi?uId=$user->{id}");
}



 


