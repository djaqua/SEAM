=head1 seam-lib.pl

 Functions for managing the Simple Email Administration Module

 foreign_require( "seam", "seam-lib.pl" );
 @sites = seam::list_seam_websites()

=cut

BEGIN { push(@INC, ".."); };
use DBI;
use WebminCore;
init_config();

my $select_domains_sql = qq~ SELECT id, name 
                             FROM virtual_domains 
                           ~;

my $select_users_sql = qq~ SELECT id, username 
                           FROM virtual_users 
                           WHERE domain=__DOMAIN__ 
                         ~;

my $update_password_sql = qq~ UPDATE virtual_users 
                              SET password=ENCRYPT(\"__PASSWORD__\") 
                              WHERE id=__ID__
                            ~;

my $database;

=head2 get_database()
    Returns the active database connection if one exists, otherwise establishes
    a new one.
=cut
sub get_database {
    if (!$database or !$database->ping) {
        $database = DBI->connect( "DBI:mysql:$DBNAME", $DBUSER, $DBPASS );
    }

    return $database;        
}

=head2 update_password(id, password)
    Updates the password for a user specified by 'id'.
=cut
sub update_password {
    
    local $sql = $update_password_sql;
    
    if ($sql =~ s/__PASSWORD__/$_[1]/g 
    and $sql =~ s/__ID__/$_[0]/g) {
        local $stmt = get_database()->prepare( $sql );                        
        $stmt->execute or die qq~                                                       
            "Whoops, $DBI::errstr"                                                      
        ~;     
        $stmt->finish();            
    }
}


=head2 get_users(domain_id)
    Returns an array of id/username hashes for all the virtual users in a
    virtual domain specified by domain_id.
=cut
sub get_users {
    
    local @users = ();
    $sql = $select_users_sql;
    
    if ($sql =~ s/__DOMAIN__/$_[0]/g) {
        $stmt = get_database()->prepare( $sql );
        $stmt->execute or die qq~ 
            "Whoops, $DBI::errstr"                                                      
        ~;
        while (@fields = $stmt->fetchrow_array) {                                  
            push( @users, {'id'=>$fields[0], 'username'=>$fields[1]} );
        }
        $stmt->finish();
    }
    return @users;    
}

=head2 get_domains()
    Returns an array of id/name hashes representing all virtual domains.
=cut
sub get_domains {
    local @domains = ();

    local $stmt = get_database()->prepare( $select_domains_sql );
    
    $stmt->execute or die qq~
            "Whoops, $DBI::errstr"
    ~;
    while (@fields = $stmt->fetchrow_array) { 
        push( @domains, {'id'=>$fields[0], 'name'=>$fields[1]} );
    }

    return @domains;
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
