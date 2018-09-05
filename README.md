# Configuration Management Kata
#### Requirements
* docker
* ansible & ansible-playbook
* pub key / private key id_rsa in your ~/.ssh keys folder so ansible can connect to the container

#### Instructions
* launch terminal and head to repo folder & run `docker-compose up -d`
* run `ansible-playbook -i inventory playbook.yml` to configure vm
* browse to localhost:8080