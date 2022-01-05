#change config ssh

file_line {'Turn off':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line {'Declare identity':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}C
