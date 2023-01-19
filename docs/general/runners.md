# GitHub Actions - Runners

## General

GitHub Actions runners are the machines that run the jobs and steps in a GitHub Actions workflow. They are responsible for executing the commands defined in the workflow file and providing the necessary resources for the tasks to be completed.

## Runner types

There are two types of runners:

- **Self-hosted runners**: These are runners that you set up and manage on your own infrastructure. This allows you to have full control over the environment in which your jobs are executed, and you can use specialized hardware or software that may not be available on the GitHub-hosted runners.

- **GitHub-hosted runners**: These are runners that are provided and managed by GitHub. They are available in multiple operating systems, and they provide a variety of environments to run your jobs. These runners are free to use for public repositories, and for private repositories you can use them for free for a certain amount of minutes per month.

## Examples

Here's an example of how to specify the runner for a job in a workflow file:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

In this example, the job is set to run on the latest version of Ubuntu, which is a GitHub-hosted runner.

You can also specify a self-hosted runner by using the name of the runner:

```yaml
jobs:
  build:
    runs-on: self-hosted
    name: my-runner
```

In this example, the job is set to run on a self-hosted runner named "my-runner".

You can also specify a matrix of runners to run the job on multiple runners:

```yaml
jobs:
  build:
    runs-on:
      - windows-latest
      - ubuntu-latest
      - macos-latest
```

In this example, the job is set to run on the latest version of Windows, Ubuntu, and macOS.

It is important to note that the choice of runner will depend on the specific requirements of your workflow, such as the operating system, software dependencies, and hardware resources needed.

Additionally, you can use the needs keyword to specify dependencies between jobs. For example, you can use it to specify that a job depends on another job to be completed before it can start:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Build
      run: make build

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - name: Test
      run: make test
```

In this example, the test job will not start until the build job is completed.

## Summary

In conclusion, GitHub Actions runners are an essential component of a GitHub Actions workflow, providing the environment and resources needed to execute the jobs and steps defined in the workflow file. Whether you choose to use self-hosted or GitHub-hosted runners, you should carefully consider the requirements of your workflow and choose the runner that best fits your needs.
