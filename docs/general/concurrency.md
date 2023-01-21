# GitHub Actions - Concurrency

## General

GitHub Actions allows you to optimize the execution time of your workflows by using the `concurrency` keyword. This keyword can be used at the workflow scope, or within a specific job, to specify how many actions can run simultaneously. In this blog post, we will explore the use of the `concurrency` keyword in GitHub Actions and provide some examples to make it clearer.

## Workflow scope

At the workflow scope, the `concurrency` keyword can be used to set a maximum number of concurrent actions that can run across all jobs in the workflow. For example:

```yaml
name: Test
on: push
concurrency: 4

jobs:
  test-python:
    runs-on: ubuntu-latest
    steps:
    - name: Run Python tests
      run: python -m unittest discover
  test-javascript:
    runs-on: ubuntu-latest
    steps:
    - name: Run JavaScript tests
      run: jest
```

In this example, the maximum number of concurrent actions that can run across all jobs is 4. This means that at most 4 jobs can run at the same time.

In addition, you can also use the `concurrency` keyword at the workflow scope with groups, which allows you to specify the maximum number of concurrent actions that can run within a group of jobs. For example:

```yaml
name: Test
on: push

workflow_dispatch:
  concurrency:
    groups:
      tests: 2

jobs:
  test-python:
    runs-on: ubuntu-latest
    group: tests
    steps:
    - name: Run Python tests
      run: python -m unittest discover
  
  test-javascript:
    runs-on: ubuntu-latest
    group: tests
    steps:
    - name: Run JavaScript tests
      run: jest
  
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Build
      run: make build
```

Here, the workflow runs on every push to the repository and the build job runs separately. We also group the test-python and test-javascript job under the same group tests. This allows you to specify a concurrency limit of 2 for the entire group of tests jobs, meaning that at most 2 tests jobs can run at the same time. This can be useful when you have a large number of tests to run and want to limit the number that run concurrently to avoid overloading the system.