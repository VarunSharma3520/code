# [Docker Basics](https://docs.docker.com/get-started/docker_cheatsheet.pdf)
**Version Information** <br>
   ```bash
   docker --version
   docker version
   docker info
   ```

**Help** <br>
   ```bash
   docker --help
   docker <command> --help
   ```

### Images
**List Images** <br>
   ```bash
   docker images
   ```

**Pull Image** <br>
   ```bash
   docker pull <image>
   ```

**Build Image** <br>
   ```bash
   docker build -t <name>:<tag
   ```

**Remove Image** <br>
   ```bash
   docker rmi <image>
   ```

**Tag Image** <br>
   ```bash
   docker tag <image> <repository>:<tag>
   ```

**Push Image** <br>
   ```bash
   docker push <repository>:<tag>
   ```

**Save Image to File** <br>
   ```bash
   docker save -o <path> <image>
   ```

**Load Image from File**<br>
    ```bash
    docker load -i <path>
    ```

### Containers
**List Running Containers**<br>
    ```bash
    docker ps
    ```

**List All Containers**<br>
    ```bash
    docker ps -a
    ```

**Run Container**<br>
    ```bash
    docker run <image>
    ```<br>
    ```bash
    docker run -d <image>
    ```<br>
    ```bash
    docker run -it <image> /bin/bash
    ```

**Start Container**<br>
    ```bash
    docker start <container>
    ```

**Stop Container**<br>
    ```bash
    docker stop <container>
    ```

**Restart Container**<br>
    ```bash
    docker restart <container>
    ```

**Remove Container**<br>
    ```bash
    docker rm <container>
    ```

**Kill Container**<br>
    ```bash
    docker kill <container>
    ```

**Pause Container**<br>
    ```bash
    docker pause <container>
    ```

**Unpause Container**<br>
    ```bash
    docker unpause <container>
    ```

**Rename Container**<br>
    ```bash
    docker rename <old_name> <new_name>
    ```

**Attach to Running Container**<br>
    ```bash
    docker attach <container>
    ```

**Exec Command in Container**<br>
    ```bash
    docker exec -it <container> <command>
    ```

### Container Logs
**View Logs**<br>
    ```bash
    docker logs <container>
    ```

**Follow Logs**<br>
    ```bash
    docker logs -f <container>
    ```

**View Last N Lines of Logs**<br>
    ```bash
    docker logs --tail <n> <container>
    ```

### Container Networking
**List Networks**<br>
    ```bash
    docker network ls
    ```

**Create Network**<br>
    ```bash
    docker network create <network>
    ```

**Inspect Network**<br>
    ```bash
    docker network inspect <network>
    ```

**Connect Container to Network**<br>
    ```bash
    docker network connect <network> <container>
    ```

**Disconnect Container from Network**<br>
    ```bash
    docker network disconnect <network> <container>
    ```

**Remove Network**<br>
    ```bash
    docker network rm <network>
    ```

### Volumes
**List Volumes**<br>
    ```bash
    docker volume ls
    ```

**Create Volume**<br>
    ```bash
    docker volume create <volume>
    ```

**Inspect Volume**<br>
    ```bash
    docker volume inspect <volume>
    ```

**Remove Volume**<br>
    ```bash
    docker volume rm <volume>
    ```

### Docker Compose
**Start Services**<br>
    ```bash
    docker-compose up
    ```<br>
    ```bash
    docker-compose up -d
    ```

**Stop Services**<br>
    ```bash
    docker-compose down
    ```

**Build Services**<br>
    ```bash
    docker-compose build
    ```

**List Services**<br>
    ```bash
    docker-compose ps
    ```

**View Logs**<br>
    ```bash
    docker-compose logs
    ```<br>
    ```
    docker-compose logs -f
    ```

### Inspect and Stats
**Inspect Container**<br>
    ```bash
    docker inspect <container>
    ```

**Container Stats**<br>
    ```bash
    docker stats <container>
    ```

**Container Top**<br>
    ```bash
    docker top <container>
    ```

### Clean Up
**Remove Stopped Containers**<br>
    ```bash
    docker container prune
    ```

**Remove Unused Images**<br>
    ```bash
    docker image prune
    ```<br>
    ```
    docker image prune -a
    ```

**Remove Unused Networks**<br>
    ```bash
    docker network prune
    ```

**Remove Unused Volumes**<br>
    ```bash
    docker volume prune
    ```

### System Commands
**Docker System Information**<br>
    ```bash
    docker system info
    ```

**Docker System Prune (Clean up everything)** <br>
    ```bash
    docker system prune
    ``` <br>
    ```bash
    docker system prune -a
    ```
