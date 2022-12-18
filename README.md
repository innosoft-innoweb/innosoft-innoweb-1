[![INNOSOFT eventos Build](https://github.com/innosoft-innoweb/innosoft-innoweb-1/actions/workflows/main.yml/badge.svg)](https://github.com/innosoft-innoweb/innosoft-innoweb-1/tree/main)
[![Docker Deployment](https://github.com/innosoft-innoweb/innosoft-innoweb-1/actions/workflows/docker.yml/badge.svg)](https://hub.docker.com/layers/innosoftinnoweb/innosoft-innoweb-1/main/images/sha256-4b3216f902c8506c4de58b5ad6f33531e467d09fca80e9c629d98ed68d67dae4?context=explore)
[![Code Quality Codacy Badge](https://app.codacy.com/project/badge/Grade/6c581ba57c024b42a96e0cdd285c87d3)](https://www.codacy.com/gh/innosoft-innoweb/innosoft-innoweb-1/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=innosoft-innoweb/innosoft-innoweb-1&amp;utm_campaign=Badge_Grade)
[![Coverage Codacy Badge](https://app.codacy.com/project/badge/Coverage/6c581ba57c024b42a96e0cdd285c87d3)](https://www.codacy.com/gh/innosoft-innoweb/innosoft-innoweb-1/dashboard?utm_source=github.com&utm_medium=referral&utm_content=innosoft-innoweb/innosoft-innoweb-1&utm_campaign=Badge_Coverage)

# <img src="https://github.com/innosoft-innoweb/innosoft-innoweb-1/blob/main/static/images/innosoft_logo-nobg.png" width="27"> Innosoft Innoweb

Website developed to support university days events where participants can register in events and consult their punctuation in those.

## Possible ways of using Innosoft Innoweb

 - [Local Installation](#local-installation) :computer:
 - [Docker Local Deployment](#docker-local-deployment) :whale:
 - [Vagrant Local Deployment](#vagrant-local-deployment) **V**
 - [Internet Deployment](#internet-deployment) :globe_with_meridians:

## Local Installation

### Pre-requirements

- [Python 3.10.5](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [MySQL](https://dev.mysql.com/downloads/installer/)

### Steps

1. To run the project locally, open a command console and run the following commands:

    ```
    pip install pipenv
    
    pipenv shell
    
    git clone https://github.com/innosoft-innoweb/innosoft-innoweb-1
  
    cd innosoft-innoweb-1
  
    pip install -r requirements.txt
    ```
    
2. This project uses environment variables that need to be set before running the project, you will need to create a file called ".env" inside the directory with the following content:

    ```
    DJANGO_SECRET_KEY = 'django-insecure-_$s8&xy9@woe3wlr(pqj3r(n8q78o4j##h-f4e%@3=ms_d$!i7'
    PRODUCTION_DB_USER = ' '
    PRODUCTION_DB_PASSWORD = ' '
    ```
    An example django secret key is given here, but the best option is to have it generated by the user himself, knowing that it is a key that is used to encrypt       sensitive data in the django application, and is at least 50 characters long.
    
3. To configure the database, it is necessary to indicate during the installation that the Setup type is full, and that the port to connect to the server will be 3307.
Once the installation is finished, we must create the database and the user that will use our project, executing the following commands line by line in a script:

    ```
    CREATE DATABASE innowebdb;
    CREATE USER 'innosoft'@'localhost' IDENTIFIED BY 'innosoft-2022';
    GRANT ALL PRIVILEGES ON `innowebdb` . * TO 'innosoft'@'localhost';
    FLUSH PRIVILEGES;
    ```
    
4. Now we will proceed to run the project, executing the following commands in a console inside the directory:

    ```
    python manage.py makemigrations

    python manage.py migrate

    python manage.py loaddata "fixtures/initial.json"

    python manage.py runserver
    ```

5. If you've gotten to this point without any errors, you should be running the project locally successfully. You can access the initial route through the following link: [http://localhost:8000](http://localhost:8000) 
   
## Docker Local Deployment

### Pre-requirements

- [Git](https://git-scm.com/downloads)
- [Docker Desktop 4.15.0](https://docs.docker.com/desktop/release-notes/)
- [WSL 2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

### Steps

1. To run the docker container locally, open a command console and run the following commands:

    ```
    git clone https://github.com/innosoft-innoweb/innosoft-innoweb-1
  
    cd innosoft-innoweb-1
    ```
    
2. This project uses environment variables that need to be set before running the project, you will need to create a file called ".env" inside the directory with the following content:

    ```
    DJANGO_SECRET_KEY = 'django-insecure-_$s8&xy9@woe3wlr(pqj3r(n8q78o4j##h-f4e%@3=ms_d$!i7'
    PRODUCTION_DB_USER = ' '
    PRODUCTION_DB_PASSWORD = ' '
    ```
    An example django secret key is given here, but the best option is to have it generated by the user himself, knowing that it is a key that is used to encrypt       sensitive data in the django application, and is at least 50 characters long.
    
 3. Once the .env file is created, run the following command in the project directory:
    
    ```
    docker-compose up -d
    ```

4. Finally, open the browser and access the following link: [http://localhost:8000](http://localhost:8000)

## Vagrant Local Deployment

### Pre-requirements

- [Git](https://git-scm.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://developer.hashicorp.com/vagrant/downloads)

### Steps

1. To run the development environment with Vagrant, open a command console and run the following commands:

    ```
    git clone https://github.com/innosoft-innoweb/innosoft-innoweb-1
  
    cd innosoft-innoweb-1
  
    cd Vagrant
    
    vagrant up
    
    vagrant ssh
    ```
    
2. Once inside the virtual machine, execute in the command line:

    ```
    cd innosoft-innoweb-1
    
    sudo python3 manage.py makemigrations --settings=innoweb.deployment_settings
    
    sudo python3 manage.py migrate --settings=innoweb.deployment_settings
    
    sudo python3 manage.py loaddata "fixtures/initial.json" --settings=innoweb.deployment_settings
    
    sudo python3 manage.py runserver 0.0.0.0:8000 --settings=innoweb.deployment_settings
    ```

    Django secret key is given in deployment_settings, but the best option is to have it generated by the user himself, knowing that it is a key that is used to encrypt sensitive data in the django application, and is at least 50 characters long.

3. Finally, open the host browser and access the following link: [http://localhost:8000](http://localhost:8000)

## Internet Deployment

In addition to all of the above, the project is deployed in PythonAnywhere in the following [link](https://innosoftinnoweb.pythonanywhere.com/).
