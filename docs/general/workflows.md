# GitHub Actions - Workflows

In the last post we learned about GitHub Actions and the capabilities it offers. In this blog post, we'll take a deep dive into the basic components of a GitHub Actions workflow and provide detailed examples and code snippets to help you understand how to create your own workflows.

## Workflow syntax

A GitHub Actions workflow is defined in a file called main.yml that lives in the .github/workflows directory of your repository. The syntax of the workflow file is based on YAML, and it consists of three main components:

- **Triggers**: These are the events that will trigger the execution of your workflow. For example, a push event to the main branch, or the creation of a pull request.

- **Jobs**: These are the individual tasks that make up your workflow. Each job is defined as a set of steps that are executed sequentially.

- **Steps**: These are the individual commands that are executed as part of a job. Steps can be defined using either JavaScript or a shell script.

Here's an example of a simple workflow file that runs on every push to the main branch:

```yaml
name: My Workflow
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3

    - name: Run tests
      run: npm test
```

This workflow has a single job called build that runs on the latest version of Ubuntu. When the workflow is triggered by a push event, it will first check out the code, and then run the npm test command.

The name key is used to give a name to the workflow, which is useful when you have multiple workflows in a single repository. The on key is used to specify the trigger for the workflow. In this case, the workflow is triggered by a push event.

It is also possible to specify multiple triggers for a workflow. Here's an example of a workflow that runs on both push and pull request events:

```yaml
name: My Workflow
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    - cron: "0 21 * * *" # at 21:00, every day
  workflow_dispatch:
```

In this example, the workflow will run in all the following scenarios:

- a push event on the main branch occurs
- a pull request is opened or updated on the main branch
- based on a schedule, here evert day at 21:00
- the workflow is run manually

## Jobs and steps

Jobs are the building blocks of a GitHub Actions workflow, and they allow you to define a set of steps that are executed sequentially. A job can be defined using the jobs key in the workflow file, and it can contain one or more steps.

Steps are the individual commands that are executed as part of a job. They can be defined using either JavaScript or a shell script. Each step must have a unique name and must specify an action or run key, which tells GitHub Actions what command to run.

Here's an example of a job with multiple steps:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Install dependencies
      run: npm c
```
