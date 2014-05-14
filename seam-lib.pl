=head1 seam-lib.pl

 Functions for managing the Simple Email Administration Module

 foreign_require( "seam", "seam-lib.pl" );
 @sites = seam::list_seam_websites()

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

=head2 get_seam_config()
 Returns the SEAM Webserver configuration as a list of hash references with 
 name and value keys.
=cut

sub get_seam_config {
    my $lref = &read_file_lines( $config{'seam_conf'} );
    my @rv;
    my $lnum = 0;

    foreach my $line (@$lref) {
        my ($n, $v) = split( /\s+/, $line, 2 );
        if ($n) {
            push( @rv, {'name'=> $n, 'value' => $v, 'line' => $lnum} );
        }
        $lnum++;
    }
    return @rv;
}
