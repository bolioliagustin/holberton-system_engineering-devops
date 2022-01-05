#change ssh config
file_line {'/etc/ssh/sshd_config':
  ensure => present,
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}
file_line {'/etc/ssh/sshd_config2':
  ensure => present,
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile /root/.ssh/school',
}
