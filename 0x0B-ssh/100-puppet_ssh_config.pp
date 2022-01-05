#change ssh config
file_line {'Turn off Passwd':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}
file_line {'Disable root login':
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile /root/.ssh/school',
}
