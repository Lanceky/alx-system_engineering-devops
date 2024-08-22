# 0-the_sky_is_the_limit_not.pp
# Increases the ULIMIT for the Nginx process

# Increase the ULIMIT in the default Nginx configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx to apply the changes
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix--for-nginx'],
}
