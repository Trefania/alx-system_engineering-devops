#Using Puppet, create a manifest that kills a process named killmenow.
#Must use the exec Puppet resource
#Must use pkill

exec { 'killmenow':
path    => ['/usr/bin'],
command => 'pkill -f killmenow'
}
