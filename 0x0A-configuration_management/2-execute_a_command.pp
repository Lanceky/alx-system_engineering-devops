# This Puppet manifest kills the 'killmenow' process using pkill.
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
