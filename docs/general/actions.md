# GitHub Actions - Actions

## General

As we have already mentioned GitHub Actions is a powerful automation tool that allows developers to create custom workflows for their projects. These workflows, or "actions," can be used to automate a wide variety of tasks, such as building and testing code, deploying code to production, and more. In this blog post, we will take a detailed look at what actions are and how to create your own using an example of building a python application in a Docker container.

## What are GitHub Actions?

In GitHub, actions are individual, reusable pieces of code that can be run in a workflow. These actions can be written in a variety of programming languages, such as JavaScript, Python, and more. Each action has a specific purpose, such as building code, running tests, or deploying code to a production environment.

Actions can be built and shared by the community, and also can be built by yourself. To create your own action, you will first need to create a new repository in GitHub. This repository will contain the code for your action, as well as any necessary configuration files. Once your repository is created, you can start writing your action.

## Components of an Action

There are two main components to an action: the action.yml file and the code file. The action.yml file is a configuration file that contains information about the action, such as its name, inputs, and outputs. The code file is where the actual code for the action is located.

Here's an example of a simple action that builds a Python application in a Docker container:

```yaml
name: "Build Python Application in Docker"
description: "This action builds a Python application in a Docker container."
inputs:
  path:
    description: "The path to the Python application."
    required: true
  image:
    description: "The Docker image to use for building the application"
    required: true
outputs:
  build_status:
    description: "The build status of the application."
runs:
  using: "docker"
  main: "entrypoint.sh"
```

In this example, the action is named "Build Python Application in Docker" and it has two inputs, path, which is the path to the Python application and image which is the Docker image to use for building the application. The action also has a single output, build_status, which is the build status of the application. The action is set to run using Docker and the main file is entrypoint.sh.

The code for this action is located in the entrypoint.sh file, which might look something like this:

```bash
#!/bin/sh

set -e

echo "Building Python application in Docker container"

docker build -t $IMAGE_NAME .

echo "Build completed successfully."

return { build_status: "success" }
```

This code uses the Docker command line to build the image using the Dockerfile in the application path and also using the image name provided as input. If the build is successful, the action will return a build_status of "success." If the build fails, the action will return a build_status of "failure."

## Using Actions in a Workflow

Once you have created your action, you can use it in a workflow. A workflow is a series of actions that are run in a specific order. Here's an example of a workflow that uses the "Build Python Application in Docker" action:

```yaml
name: Build and Deploy
on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Build Application
      uses: ./ #path to your action
      with:
        path: 'path/to/my/app'
        image: 'my_image_name'

    - name: Deploy Application
      run: |
        # commands to deploy the application
        # e.g. `docker push` or `kubectl apply`
```

In this example, the workflow is named "Build and Deploy" and it is triggered by a push to the main branch. The workflow contains a single job called "build" that runs on the latest version of Ubuntu. The job has three steps:

1. Check out the code using the actions/checkout action
2. Build the application using the custom action ./ (path to your action)
3. Deploy the application using your custom command (e.g. docker push or kubectl apply)

You can add additional steps to the job, such as running tests, or you can add additional jobs for different stages of the pipeline, such as "test" and "deploy." And also you can use the output of your custom action as input for another action.

With GitHub Actions, you have the flexibility to create custom workflows that fit the needs of your project. Whether you're building a simple application or a complex microservices architecture, GitHub Actions can help you automate your development pipeline and streamline your workflow.
