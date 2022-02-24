#Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec {'remove':
  command => 'sed -rie \'s/(holberton (hard|soft) nofile).*/\1 1000/gi\' /etc/security/limits.conf',
  path    => 'usr/bin/:/bin/'
}
