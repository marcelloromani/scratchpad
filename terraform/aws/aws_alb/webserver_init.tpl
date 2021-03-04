#!/bin/bash
yum -y install httpd

# IMPORTANT!
sed -i 's;Listen 80;Listen 0.0.0.0:80;g' /etc/httpd/conf/httpd.conf

PUBLIC_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)

echo "<h1>Welcome to ${project}</h1>" >> /var/www/html/index.html
echo "<p>Public IP: $PUBLIC_IP</p>" >> /var/www/html/index.html
echo "<p>Instance ID: $INSTANCE_ID</p>" >> /var/www/html/index.html

service httpd start
chkconfig httpd on
