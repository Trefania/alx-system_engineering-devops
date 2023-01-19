# include stdlib
# # sudo apt update -y
# exec { "Update Apt Repos":
#   command => "sudo apt update",
#   path    => "/usr/bin/"
# }

# #sudo apt upgrade -y
# exec { "Run Upgrade":
#   command => "sudo apt upgrade",
#   path    => "/usr/bin/",
#   require => Exec["Update Apt Repos"]
# }
# # sudo apt install nginx -y
# package { "nginx":
#   ensure  => "installed",
#   require => Exec["Run Upgrade"]
# }
# # sed -i "/listen 80 default_server/i add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
# file_line {"append_string":
#     ensure  => "present",
#     path    => "/etc/nginx/sites-available/default",
#     after   => "listen 80 default_server",
#     line    => "add_header X-Served-By $HOSTNAME;",
#     require => Package["nginx"]
# }
# # sudo service nginx restart
# service { "nginx":
#   ensure  => running,
#   require => File_line["append_string"]
# }

exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
