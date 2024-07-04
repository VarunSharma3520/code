# Docker Basics
**Version Information** <br>
   ```
   docker --version
   docker version
   docker info
   ```

**Help** <br>
   ```
   docker --help
   docker <command> --help
   ```

### Images
**List Images** <br>
   ```
   docker images
   ```

**Pull Image** <br>
   ```
   docker pull <image>
   ```

**Build Image** <br>
   ```
   docker build -t <name>:<tag
   ```

**Remove Image** <br>
   ```
   docker rmi <image>
   ```

**Tag Image** <br>
   ```
   docker tag <image> <repository>:<tag>
   ```

**Push Image** <br>
   ```
   docker push <repository>:<tag>
   ```

**Save Image to File** <br>
   ```
   docker save -o <path> <image>
   ```

**Load Image from File**<br>
    ```
    docker load -i <path>
    ```

### Containers
**List Running Containers**<br>
    ```
    docker ps
    ```

**List All Containers**<br>
    ```
    docker ps -a
    ```

**Run Container**<br>
    ```
    docker run <image>
    ```<br>
    ```
    docker run -d <image>
    ```<br>
    ```
    docker run -it <image> /bin/bash
    ```

**Start Container**<br>
    ```
    docker start <container>
    ```

**Stop Container**<br>
    ```
    docker stop <container>
    ```

**Restart Container**<br>
    ```
    docker restart <container>
    ```

**Remove Container**<br>
    ```
    docker rm <container>
    ```

**Kill Container**<br>
    ```
    docker kill <container>
    ```

**Pause Container**<br>
    ```
    docker pause <container>
    ```

**Unpause Container**<br>
    ```
    docker unpause <container>
    ```

**Rename Container**<br>
    ```
    docker rename <old_name> <new_name>
    ```

**Attach to Running Container**<br>
    ```
    docker attach <container>
    ```

**Exec Command in Container**<br>
    ```
    docker exec -it <container> <command>
    ```

### Container Logs
**View Logs**<br>
    ```
    docker logs <container>
    ```

**Follow Logs**<br>
    ```
    docker logs -f <container>
    ```

**View Last N Lines of Logs**<br>
    ```
    docker logs --tail <n> <container>
    ```

### Container Networking
**List Networks**<br>
    ```
    docker network ls
    ```

**Create Network**<br>
    ```
    docker network create <network>
    ```

**Inspect Network**<br>
    ```
    docker network inspect <network>
    ```

**Connect Container to Network**<br>
    ```
    docker network connect <network> <container>
    ```

**Disconnect Container from Network**<br>
    ```
    docker network disconnect <network> <container>
    ```

**Remove Network**<br>
    ```
    docker network rm <network>
    ```

### Volumes
**List Volumes**<br>
    ```
    docker volume ls
    ```

**Create Volume**<br>
    ```
    docker volume create <volume>
    ```

**Inspect Volume**<br>
    ```
    docker volume inspect <volume>
    ```

**Remove Volume**<br>
    ```
    docker volume rm <volume>
    ```

### Docker Compose
**Start Services**<br>
    ```
    docker-compose up
    ```<br>
    ```
    docker-compose up -d
    ```

**Stop Services**<br>
    ```
    docker-compose down
    ```

**Build Services**<br>
    ```
    docker-compose build
    ```

**List Services**<br>
    ```
    docker-compose ps
    ```

**View Logs**<br>
    ```
    docker-compose logs
    ```<br>
    ```
    docker-compose logs -f
    ```

### Inspect and Stats
**Inspect Container**<br>
    ```
    docker inspect <container>
    ```

**Container Stats**<br>
    ```
    docker stats <container>
    ```

**Container Top**<br>
    ```
    docker top <container>
    ```

### Clean Up
**Remove Stopped Containers**<br>
    ```
    docker container prune
    ```

**Remove Unused Images**<br>
    ```
    docker image prune
    ```<br>
    ```
    docker image prune -a
    ```

**Remove Unused Networks**<br>
    ```
    docker network prune
    ```

**Remove Unused Volumes**<br>
    ```
    docker volume prune
    ```

### System Commands
**Docker System Information**<br>
    ```
    docker system info
    ```

**Docker System Prune (Clean up everything)** <br>
    ```
    docker system prune
    ``` <br>
    ```
    docker system prune -a
    ```
