#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
service nginx restart
