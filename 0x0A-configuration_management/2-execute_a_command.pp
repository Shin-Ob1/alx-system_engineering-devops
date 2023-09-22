# Executes a command

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
