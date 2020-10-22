#! /bin/bash

# Update and upgrade ubuntu OS
sudo apt update -y
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y

# Add RTMP module and repos
sudo add-apt-repository universe
sudo apt install libnginx-mod-rtmp -y

# Replace current nginx configuration with RTMP enabled configuration
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bk
cp nginx.conf /etc/nginx/nginx.conf

