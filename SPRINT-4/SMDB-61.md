# Containerization

## What are microservices

Microservices is an architectural style that structures an application as a collection of services that are highly maintainable and testable, loosely coupled, independently deployable, organized around business capabilities, and owned by a small team.

The microservices architecture enables the rapid, frequent, and reliable delivery of large, complex applications. It also enables an organization to evolve its technology stack.

## What is Docker

Docker is a software framework for building, running, and managing containers on servers and the cloud.

It allows you to package code and all of its dependencies in containers.

A docker image contains everything needed to run an application: code, runtime, system tool, system libraries, and settings; but it shares the kernel with the host machine.

## Top commands for Docker

- `docker version`
- `docker run`
- `docker ps`
- `docker exec`
- `docker stop`
- `docker build`
- `docker pull`
- `docker kill`
- `docker images`
- `docker rm`
- `docker restart`
- `docker rmi`
- `docker cp`

## Dockerfile

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

## Build a Dockerfile

`$ docker build .`
`$ docker build -f Dockerfile.dev .`

## Docker image registry

A Docker registry is a storage and distribution system for named Docker images. The same image may have multiple versions identified by their tags.

### Main Docker registries

- Docker Hub
- Azure Container Registry
- Amazon ECR
- Google Container Registry
- Gitlab Container Registry

### Push to registry

`$ docker login`
`$ docker build .`
`$ docker tag <image> <registry-user>/<repo-name>[:<tag>]`
`$ docker push <registry-user>/<repo-name>:<tag>`

## Docker Compose

Compose is a tool for defining and running multi container docker applications.

With Compose, you use a YAML file to configure your application's services. Then, with a single command, you can create and start all the services from your configuration.
