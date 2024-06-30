# This uninstalls all docker container, images, volumes

### Stop all running containers
```docker stop $(docker ps -q)```

### Remove all containers
```docker rm $(docker ps -a -q)```

### Remove all images
```docker rmi $(docker images -q)```

### Optional - Remove all volumes
```docker volume rm $(docker volume ls -q)```

### Optional - Remove all networks
```docker network rm $(docker network ls -q)```