# MAP - Development Environment

## Description
This directory contains all that is required to spin-up a local development environment for the MAP project.

## Requirements
- Docker
- `docker-compose`

## Usage
### Spin up development environment
`sh start.sh`

### Useful Commands
##### List running containers
`docker ps`
##### Connect to container
`docker exec -u root -it <container_name> /bin/bash`