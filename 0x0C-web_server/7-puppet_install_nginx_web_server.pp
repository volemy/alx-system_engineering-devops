# Install nginx web server
package { 'nginx':
  ensure => installed
}

# Configure a redirect to Pinterest in the default Nginx site configuration
file_line { 'nginx_redirect_configuration':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.pinterest.com/pin/758997343472891932/ permanent;',
}

# Create an index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
