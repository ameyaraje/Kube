# Kube

This is a simple Python app using Flask that I'm creating to deploy to a Kubernetes cluster.

Steps to run:
1. Install Docker
2. Build the Docker image using the Dockerfile
    `docker build -f Dockerfile . -t <name-of-image>`
3. Run the image created 
    `docker run -d <name-of-image>`