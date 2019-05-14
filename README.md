# bw_monitor_ex

Ubuntu 18.10

install windows bash shell

ssh root@<ip address>

apt update && apt upgrade

hostnamectl set-hostname flask-server
hostname

nano /etc/hosts
<ip address>  flask-server

adduser <username>
adduser <username> sudo

exit

ssh <username>@<ip address>

mkdir .ssh

(local machine windows bash)
ssh-keygen -b 4096

move .pub to server
scp ~/.ssh/id_rsa.pub <username>@<ip address>:~/.ssh/authorized_keys

(server)
ls .ssh
key copied there.

sudo chmod 700 ~/.ssh/

sudo chmod 600 ~/.ssh/*
---- ssh key working ----

sudo nano /etc/ssh/sshd_config

PermitRootLogin no

PasswordAuthentication no

save


sudo systemctl restart sshd

-----------
sudo apt install ufw

sudo ufw default allow outgoing

sudo ufw default deny incoming

sudo ufw allow ssh

sudo ufw allow 5000

sudo ufw enable

sudo ufw status
------------

git clone

or scp
(local machine)
scp -r Desktop/Flask_Blog <username>@<ip address>:~/


sudo apt install python3-pip
sudo apt install python3-venv

python3 -m venv Flask_Blog/venv
cd Flask_Blog/
source venv/bin/activate

pip install -r requriements.txt
pip install -r requirements.txt  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

(local machine)
python console

import os

os.environ.get('SECRET_KEY')
os.environ.get('SQLALCHEMY_DATABASE_URI')


(server)
sudo touch /etc/config.json

sudo nano /etc/config.json
{
  "SECRET_KEY": <KEY>,
  "SQLALCHEMY_DATABASE_URI": <URI>
}

save

flaskblog/config.py

import json
with open('/etc/config.json') as config_file:
  config = json.load(config_file) //config now is a python dictionary
  
secret_key = config.get('SECRET_KEY')
...

python run.py

or
export FLASK_APP=run.py
flask run --host=0.0.0.0

-------------------------

sudo apt install nginx

pip install gunicorn

sudo rm /etc/nginx/sites-enabled/default

sudo nano /etc/nginx/sites-enabled/flaskblog

server {
  listen 80;
  server_name <ip address>;
  
  location /static {
    alias /home/<username>/Flask_Blog/flaskblog/static;
  }
  
  location / {
    proxy_pass http://localhost:8000;
    include /etc/nginx/proxy_params;
    proxy_redirect off;
  }
}

save

sudo ufw allow http/tcp

sudo ufw delete allow 5000

sudo ufw enable

sudo systemctl restart nginx

nporc --all 
worker = 2 * core + 1

gunicorn -w 3 run:app

-----------------------

sudo apt install supervisor

sudo nano /etc/supervisor/conf.d/flaskblog.conf

[program:flaskblog]
directory=/home/<username>/Flask_Blog
command=/home/<username>Flask_Blog/venv/bin/gunicorn -w 3 run:app
user=<username>
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskblog/flaskblog.err.log
stdout_logfile=/var/log/flaskblog/flaskblog.out.log

save

sudo mkdir -p /var/log/flaskblog

sudo touch /var/log/flaskblog/flaskblog.err.log
sudo touch /var/log/flaskblog/flaskblog.out.log

sudo supervisorctl reload

-----------------------------

config nginx

sudo nano /etc/nginx/nginx.conf

client_max_body_size 5M;


sudo systemctl restart nginx





