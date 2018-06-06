# SIGOP-API
API for SIGOP android app

# Setup

- Install Python 2.7
- Install and configure MySQL
  - On Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
- Load SIGOP db to your mysql:
  - $ mysql -u admin -p -h localhost < file.sql
- Create a user and setup permissions on mysl:
  - $ sudo mysql
  - Create a username = admin and a password = senha
    - Follow this steps: https://www.digitalocean.com/community/tutorials/como-criar-um-novo-usuario-e-conceder-permissoes-no-mysql-pt
- Install virtualenv
  - $ sudo apt install virtualenv
- Create a virtualenv
  - $ virtualenv <env_name>
- Enter your env
  - $ source <env_name>/bin/activate
- Clone this repository
- Go to repository folder
- Install requirements
  - $ pip install -r requirements.txt
- Run Flask
  - IF FIRST TIME: % export FLASK_APP=app.py
  - $ flask run
