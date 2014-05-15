=head1 seam-lib.pl

 Functions for managing the Simple Email Administration Module

 foreign_require( "seam", "seam-lib.pl" );
 @sites = seam::list_seam_websites()

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

my $select_usernames = "SELECT id, username FROM virtual_users WHERE domain=2";


sub get_usernames {
    
    my @users;

    my $database = DBI->connect( "DBI:mysql:$DBNAME", $DBUSER, $DBPASS );

    my $stmt = $database->prepare( $select_usernames );
    $stmt->execute or die qq~
        Simple Email Administration Modules says:
        "Whoops, $DBI::errstr"
    ~;

    print "Hello?";
        
    while (@fields = $stmt->fetchrow_array) {
        print "id: $fields[0], <br> username: $fields[1]";
        push( @users, {'id'=> $fields[0], 'username' => $fields[1]} );
    }

    $stmt->finish();
    $database->disconnect();

    return @users;
}



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

# 
# TODO come back and use built-in module configuration capabilities             
# (/etc/webmin/seam/config)                                                     
#
open(CONF, '/root/seam.conf');                                                  
while (<CONF>) {                                                                
                                                                                
    chomp;                                                                      
    my @line = split('=', $_);                                                  
                                                                                
    if ("username" eq $line[0]) {                                               
        $DBUSER = $line[1];                                                     
    } elsif ("password" eq $line[0]) {                                          
        $DBPASS = $line[1];                                                     
    } elsif ("database" eq $line[0]) {                                          
        $DBNAME = $line[1];                                                     
    }                                                                           
                                                                                
}                                                                               
close(CONF);  
