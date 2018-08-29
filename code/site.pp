exec { 'apt':
    command => '/usr/bin/apt-get update',
}

package {'nginx':
    ensure => installed,    
}