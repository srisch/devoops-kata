Stack consists of  nginx / flask & gunicorn / mongodb
#### Requirements
* docker
* ansible & ansible-playbook
* pub key / private key id_rsa in your ~/.ssh keys folder so ansible can connect to the container

#### Instructions
* launch terminal and head to repo folder & run `docker-compose up -d`
* run `ansible-playbook -i inventory playbook.yml` to configure vm
* browse to localhost:8080

#### Next Steps
* css styling, red / green
* separate services on different containers
* pull something from mongodb
* fix mongodb service


# Configuration Management Kata
Install/configure the CM tool of your choice.

Automate the provisioning of a 3-tier web application stack (data layer, application layer, presentation layer). An example stack might be, but is in no way limited to, redis/passenger/nginx.

Automate the deployment of a simple 'ping' page that establishes that each of the 3 layers in the stack are available.

Provide us with access to your repository and identify a few issues that represent the next features to be delivered in your application. Don't be surprised if someone commits a change that addresses one of the issues. Your project should be complete as delivered, but every project has a 'next step' and we'd like to know what you think your next steps are.

