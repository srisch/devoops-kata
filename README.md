# Configuration Management Kata
#### Requirements
* docker

#### Instructions
* launch terminal and head to repo folder & run `docker-compose up -d`
* then run in your terminal `docker run --rm -p 8080:80 --net puppet puppet/puppet-agent-ubuntu agent --verbose --no-daemonize --summarize`
* Note : if you receieve a SSL error wait a few seconds and try again, this is usually because the server's services aren't running yet