#!/bin/bash
apt update -y
apt install -y nginx
systemctl enable nginx
systemctl restart nginx
echo "Hello from Terraform user_data" > /var/www/html/index.html