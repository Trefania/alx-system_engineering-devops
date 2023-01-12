#Puppet script that create ssh configuration file
include stdlib

file_line { 'Off the Password Authentication':
	ensure => 'present',
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no',
}

file_line { 'file_location':
	ensure =>'present',
	path   => 'etc/ssh/ssh_config',
	line   => 'IdentityFile ~/.ssh/school'
}