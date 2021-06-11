#!/bin/bash

# Copy the docker compose yaml to the manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@ansible-manager:/home/jenkins/docker-compose.yaml

# Deploy the Docker Stack
ssh -i ~/.ssh/ansible_id_rsa jenkins@ansible-manager "docker stack deploy --compose-file docker-compose.yaml lottery"