# changes configuration file
file { '~/.ssh/config':
    ensure => 'file',
    content => 'IdentityFile ~/.ssh/school
                PasswordAuthentication no'
}
