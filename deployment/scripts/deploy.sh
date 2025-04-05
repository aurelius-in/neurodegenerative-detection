#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
IMAGE_NAME="my-application-image"
IMAGE_TAG="latest"
NAMESPACE="default"
DEPLOYMENT_NAME="my-application"
DEPLOYMENT_FILE="../kubernetes/deployment.yaml"

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME:$IMAGE_TAG ../../

# Push the Docker image to the container registry
# Ensure you're authenticated to the registry before pushing
echo "Pushing the Docker image to the container registry..."
docker push $IMAGE_NAME:$IMAGE_TAG

# Deploy the application to Kubernetes
echo "Deploying the application to Kubernetes..."
kubectl apply -f $DEPLOYMENT_FILE -n $NAMESPACE

# Verify the deployment
echo "Verifying the deployment..."
kubectl rollout status deployment/$DEPLOYMENT_NAME -n $NAMESPACE

echo "Deployment completed successfully."
