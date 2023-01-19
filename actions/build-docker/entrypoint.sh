#!/bin/sh

set -e

echo "Building Python application in Docker container"

docker build -t $IMAGE_NAME .

echo "Build completed successfully."

return { build_status: "success" }