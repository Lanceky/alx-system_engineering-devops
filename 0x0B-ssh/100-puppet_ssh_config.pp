# Puppet manifest to configure SSH client settings

#This ensures the SSH config directory exists
file { '/home/vagrant/.ssh':
  ensure => directory,
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0700',
}

#this ensures the SSH config file exists
file { '/home/vagrant/.ssh/config':
  ensure  => file,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
}

# Ensures the IdentityFile line is present in the SSH config file
file_line { 'Declare identity file':
  path  => '/home/vagrant/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => 'IdentityFile',
}

# Ensures the PasswordAuthentication line is present and set to 'no'
file_line { 'Turn off passwd auth':
  path  => '/home/vagrant/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => 'PasswordAuthentication',
}

