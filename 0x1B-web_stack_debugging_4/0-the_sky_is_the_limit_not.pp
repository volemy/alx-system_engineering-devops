# puppet to Adjust Nginx ULIMIT and restart
# using ApacheBench for benchmarking

exec {'nginx fix':
	command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
	path => '/usr/local/bin/:/bin/'
} ->

# Restart nginx to apply changes
exec {'nginx-restart':
	command => '/etc/init.d/nginx restart',
	path => '/etc/init.d'
}
