# SIGOP-API
API for SIGOP android app

# Setup

- Install Python 2.7
- Install and configure MySQL
  - On Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
- Load SIGOP db to your mysql:
  - $ mysql < file.sql
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
