# Docker
1. Benefits:
    - Accelerate Developer onboarding
    - Eliminate App Conflicts
    - Environment Consistency
    - Ship software faster
    
2. Docker images and containers rely on a layered file system

## Docker Image
- A read-only template composed of layered filesystems used to share common files and create Docker container instances.
- Example: Ubuntu with Flask and application code

## Docker Container
- An isolated and secured shipping container created from an image that can be run, started, stopped, moved and deleted.
- Created by using an image. Runs application

### Docker run:
1. Docker client
2. Linux or Windows
3. Docker Engine (Daemon)
4. Linux Container Support (LXC) or Windows Server Container Support

### Virtual Machine (VM) architecture
1. Host operating system
2. Hypervisor
3. Guest OS
4. Bins/Libs
5. App

### Docker Container architecture
1. Host operating system
2. Docker Engine
3. Bins/Libs
4. App

### Docker Client
1. Interact with Docker Engine
2. Build and manage images
3. Run and manage containers

### Source code into container
1. Create a container volume that points to the source code.
2. Add your source code into a custom image that is used to create a container.

### Volume
1. Special type of directory in a container, typically referred to as a "data volume"
2. Can be shared and reused among containers
3. Updated to an image won`t affect a data volume
4. Data volumes are persisted even after the container is deleted.

### Docker container linking options
1. Use legacy linking
   - Run a container with a name
   - Link to running container by name
   - Repeat for additional containers
2. Add Container to a Bridge Network (preferred)
    - Create a custom bridge network
    - Run containers in the network


## Docker CLI

```bash

# docker image commands
docker pull [image name]
docker images
docker rmi [image ID]

docker build -t pawelkonior/alegrosz .
docker push pawelkonior/alegrosz

# docker container commands
docker run [image name]
docker run -d --name my-postgres postgres
docker run -d -p 5000:5000 --link my-postgres:postgres pawelkonior/alegrosz

docker ps -a 
docker rm [container ID]
docker rm -v [container ID] # removes volume
docker inspect [container ID]

docker network create --driver bridge isolated_network
docker run -d --net=isolated_network --name my-postgres postgres

docker run -p 5003:5003 -v ~/projects/flask_docker:/var/code pawelkonior/flask_docker:v4

```

## DockerFile
1. Text file used to build Docker images
2. Contains build instructions
3. Instructions create an intermediate image that can be cached to speed up future builds
4. Each Dockerfile starts with a FROM instruction

```dockerfile

FROM python:latest

LABEL author="pawel.konior@gmail.com"

ENV FLASK_APP="app"
ENV FLASK_ENV="development"
ENV PORT=5000

WORKDIR /var/code
COPY . .

RUN pip install -r requirements.txt

EXPOSE $PORT

ENTRYPOINT ["flask", "run"]

```

## Docker compose
1. Manages the whole application lifecycle
    - Start, stop and rebuild services
    - view the status of running services
    - stream the log output of running services
    - run a one-off command on a service
    
2. Key services options
    - build
    - environment
    - image
    - networks
    - ports
    - volumes
    
```yaml

version: 3.8
services:
  node:
    build:
      context: .
      dockerfile: node.dockerfile
    networks:
      - nodeapp-network
  mongodb:
    image: mongo
    networks:
      - nodeapp-network
networks:
  nodeapp-network:
    driver: bridge

```


### Docker compose cli

```bash

docker-compose buid
docker-compose up
docker-compose down
docker-compose logs
docker-compose ps
docker-compose stop
docker-compose start
docker-compose rm


docker-compose down --rmi all --volumes

```

## Kubernetes
Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

1. Container and cluster management
2. Supported by all major cloud platform
3. Provides a declarative way to define a cluster`s state using manifest files (YAML)
4. Interact with K8s using kubectl

## Kubernetes key features
1. Service discovery/ Load balancing
2. Storage Orchestration
3. Automate Rollouts/Rollbacks
4. Manage workloads
5. Self-healing
6. Secret and configuration management
7. Horizontal scaling

## K8s key elements:
1. Cluster
2. Node
3. Pod

## k8s key sources
1. Deployment
    - describe desired state
    - can be used to replicate pods
    - support rolling updates and rollbacks
    
2. Service
    - pods live and die
    - services abstract pod IP addresses from consumers
    - load balances between pods
    
### Migrating from Docker Compose to K8s
1. Compose on Kubernetes
2. Kompose


## Kubectl (kubernetes controller) CLI

```bash

kubectl version
kubectl get [deployments | services | pods]
kubect run nginx-server --image=nginx:alpine
kubectl apply -f [fileName | folderName]
kubectl port-forward [name-of-pod] 8080:80

kubectl delete -f [fileName | folderName]


```
