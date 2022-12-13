#Kills a process using puppet
exec { 'killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => 'shell'
    returns  => [0, 1],
}
