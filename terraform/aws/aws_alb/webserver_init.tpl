#!/bin/bash
yum -y install httpd

# IMPORTANT!
sed -i 's;Listen 80;Listen 0.0.0.0:80;g' /etc/httpd/conf/httpd.conf

echo "<h1>Welcome to ${project}</h1>" >> /var/www/html/index.html
service httpd start
chkconfig httpd on
