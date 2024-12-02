# This uninstalls all docker container, images, volumes

### Stop all running containers
```bash
docker stop $(docker ps -q)
```

### Remove all containers
```bash
docker rm $(docker ps -a -q)
```

### Remove all images
```bash
docker rmi $(docker images -q)
```

### Optional - Remove all volumes
```bash
docker volume rm $(docker volume ls -q)
```

### Optional - Remove all networks
```bash
docker network rm $(docker network ls -q)
```
