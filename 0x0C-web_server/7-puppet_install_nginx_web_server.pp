# manifest to perform a 301 redirect when querying /redirect_me
include stdlib

$redirect = "
        location ~/redirect_me {
            return 301 https://github.com/Trefania;
        }"

# Updating nginx
exec { 'Update':
    command => 'sudo apt update',
    path    => '/usr/bin/'
}
package { 'nginx':
    ensure => 'installed',
}

# config nginx
file_line { 'Adding redirect':
    ensure => 'present',
    path   => '/etc/nginx/sites-enabled/default',
    after  => 'server_name _;',
    line   => $redirect,
}

# content
file { '/var/www/html/index.html':
    content => 'Hello World!',
}

# beg nginx
service {'nginx':
    ensure  => running,
    require => Package['nginx'],
}