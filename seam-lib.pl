=head1 seam-lib.pl

 Functions for managing the Simple Email Administration Module

 foreign_require( "seam", "seam-lib.pl" );
 @sites = seam::list_seam_websites()

=cut

BEGIN { push(@INC, ".."); };
use WebminCore;
init_config();

$select_users = "SELECT id, username FROM virtual_users WHERE domain=25";
$select_users_sql = qq~ SELECT id, username 
                        FROM virtual_users 
                        WHERE domain=__DOMAIN__ ~;

my $database;

sub get_database {
    if (!$database or !$database->ping) {
        $database = DBI->connect( "DBI:mysql:$DBNAME", $DBUSER, $DBPASS );
    }

    return $database;        
}

sub update_password {
    my $sql = "UPDATE virtual_users SET password=ENCRYPT(\"$_[1]\") WHERE id=$_[0]";
#    print "$sql \n";
    my $stmt = get_database()->prepare( $sql );                        
    $stmt->execute or die qq~                                                       
        "Whoops, $DBI::errstr"                                                      
    ~;                    

}



sub get_users {
    my @users = ();
    
    $sql = $select_users_sql;
    
    if ($sql =~ s/(__)DOMAIN(__)/$_[0]/g) {
        $stmt = get_database()->prepare( $sql );
        $stmt->execute or die qq~ 
            "Whoops, $DBI::errstr"                                                      
        ~;
#        print "where we should be ...";
        while (@fields = $stmt->fetchrow_array) {                                  
            #print qq~<option value="$fields[0]">$fields[1]</option>~;
#            print "User: $fields[1] <br>";
            push( @users, {'id'=>$fields[0], 'username'=>$fields[1]} );
        }

    }

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
