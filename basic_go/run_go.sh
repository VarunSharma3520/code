#!/bin/bash

# cleanup
sudo docker stop $(sudo docker ps -a -q) #stops all container
sudo docker rm $(sudo docker ps -a -q) #removes all container
sudo docker rmi learngo #removes learngo
sudo docker image prune -y #removes all dangling images

#building container
sudo docker build -t learngo . #build container

#list of container and images
sudo docker images -a #list all images
sudo docker ps -all #list all container

echo ""
echo ""
echo ""
echo ""
echo ""
echo ""
sudo docker run -i -p 8080:8080 -v "$(pwd)"/:/app learngo #run container
