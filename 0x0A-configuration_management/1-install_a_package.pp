package { 'flask':
# the version that is currently running
  ensure   => '2.1.0',
#using pipe
  provider => 'pip3'
}