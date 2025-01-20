<div align="center">
<h1 align="center">Django Online Shop</h1>
<h3 align="center">It's my biggest peroject that i've ever done, I spent a lot of time on it</h3>
</div>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://jquery.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jquery/jquery-vertical.svg" alt="jquery" width="60" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
<a href="https://redis.io" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/> </a>
<a href="https://www.gunicorn.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg" alt="gunicorn" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/nginx/nginx-icon.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg" alt="nginx" width="40" height="40"/> </a>
</p>

# Guideline
- [Goal](#goal)
- [Extera features](#extera-features)
- [Setup](#setup)
    - [First step](#first-step)
    - [Clone it](#clone-it)
    - [Docker](#docker)
        - [Development](#development)
            - [Django Debug Toolbar](#pytest)
            - [Pytest](#django-debug-toolbar)
            - [Flake8 and Black](#flake8-and-black)
        - [Deployment](#deployment)
            - [Gunicorn and Nginx](#gunicorn-and-nginx)
- [DB schema](#db-schema)
            


# Goal
I create this website for testing all skills that i've learned

# Extera features
I added a lot of useful tools to make this site better, These features include :

### Development & Deployment
I separate all codes and files for use it on [Development](#development) or [Deployment](#deployment)

### Caching system
I used redis for caching system in my project

### Reformatted code
I reformat all codes depends on PEP8 rule with [Flake8 and Black](#flake8-and-black)

### Testing system
I used [Pytest](#pytest) for testing system and test various parts of site

### Documents
I leave a full documention about how the website works in <a href='https://github.com/Benfoxyy/Django-Online-Shop/blob/main/Documents/'>Documents</a> folder

### Various User
This shop has 3 types of user :
- customer
- admin
- superuser

Each of them has a specific profile that has own properties

# Setup

## First step
For setup this site and walk through it you need to have <a href='https://www.docker.com/'>docker</a> on you computer

## Clone it
Next step is cloning this project
```bash
git clone https://github.com/Benfoxyy/Django-Online-Shop.git
```

## Docker
Docker is a powerful tool for run, deploying and transferring project, so i decided to use it .

As i said i separet my site, so for run it on development or deployment mode, you should follow one of these section :

## Development
```bash
docker-compose up --build -d
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1:8000'>127.0.0.1:8000</a> on your browser to see the resault

This version of website is for <b>developers</b> to testing and editting

This version has some tools that it is not exist in [Deployment](#deployment) like :

### Django Debug Toolbar
<a href='https://pypi.org/project/django-debug-toolbar/'>django_debug_toolbar</a> is an useful library for django to get reports of every single page and manage it better

### Pytest
<a href='https://docs.pytest.org/en/stable/'>pytest</a> is the most powerful testing system for python, for using it enter this command :
```bash
docker-compose exec backend sh -c "pytest"
```

### Flake8 and Black
As i said <a href='https://pypi.org/project/flake8-django/'>Flake8</a> and <a href='https://pypi.org/project/black/'>Black</a> are helping for reformat all codes by <a href='https://peps.python.org/pep-0008/'>PEP8</a> rule, for using enter this command :
```bash
docker-comopose exec backend sh -c "black . -l 78 && flake8"
```

## Deployment
```bash
docker-compose -f docker-compose-deployment.yml up --build -d
```
By running this command everything creat and run automaticlly, after everything is over you can oppen <a href='127.0.0.1'>127.0.0.1</a> on your browser to see the resault

This version of website is for <b>normal user</b> to take a look to site

This version has some tools that it is not exist in [Development](#development) like :

### Gunicorn and Nginx
To set your project to deployment mode, you have to change DEBUG mode to False . This thing is a good way to make your site more secure but there is a disadvantages, statics and medias doesn't serve moreover django can't transfer requests on website so it's the time that <a href='https://gunicorn.org/'>Gunicorn</a> and <a href='https://nginx.org/en/'>Nginx</a> come .

# DB schema
<img src='./Documents/DB-diagram.png'>

<div align="center">
<h1 align="center">Thanks for visiting</h1>
<h3 align="center">I hope that you enjoy it, Let me know if you have any suggestion</h3>
</div>