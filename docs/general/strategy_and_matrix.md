# GitHub Actions - Strategy & Matrix

## General

The `strategy` and `matrix` keywords in GitHub Actions are powerful tools for implementing parallel workflows. These keywords allow you to define multiple combinations of inputs that should be run in parallel, greatly speeding up your workflow and increasing its reliability. In this blog post, we will explore the strategy and matrix keywords in depth, and provide examples of how to use them to implement parallel workflows in your own projects.

## Strategy

The `strategy` keyword is used to define a parallel strategy for your workflow. It is typically used in conjunction with the `matrix` keyword, which allows you to define multiple combinations of inputs that should be run in parallel. The strategy keyword takes a single object, which can contain the following properties:

- `matrix`: This property is used to define a matrix of inputs that should be run in parallel. The matrix property takes an object, where the keys are the names of the inputs and the values are arrays of possible values for each input.

- `fail-fast`: This property is used to specify whether the workflow should fail as soon as one job fails. The default value is false, which means that the workflow will continue running even if one job fails.

- `max-parallel`: This property is used to specify the maximum number of jobs that should run in parallel.

Here is a simple workflow that runs multiple tests in parallel:

```yaml
name: Test

on:
  workflow_dispatch:

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [8, 10, 12]
    runs-on: ${{ matrix.os }}
    steps:
    - name: Test
      run: make test
```

In this example, the `strategy` keyword is used to define a parallel matrix of test combinations. The `matrix` keyword is used to specify that the workflow should run on three different operating systems (ubuntu-latest, windows-latest, and macos-latest) and three different versions of Node.js (8, 10, and 12). This means that the workflow will run a total of 9 test combinations in parallel, rather than sequentially.

It's also possible to define parallel workflows for multiple branches. For example, if you have a workflow that runs tests on multiple branches, you can run the tests in parallel on each branch in the following way:

```yaml
name: Test

on:
  push:
    branches:
    - main
    - dev
    - feature/*

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [8, 10, 12]
    runs-on: ${{ matrix.os }}
    steps:
    - name: Test
      run: make test
```

Here, the `strategy` keyword is used to run the tests in parallel on the main, dev, and feature/* branches. This means that the workflow will run a total of 9 test combinations in parallel on each branch, rather than sequentially.

## Matrix

The `matrix` keyword is used in conjunction with the strategy keyword to define a matrix of inputs that should be run in parallel. It takes an object, where the keys are the names of the inputs and the values are arrays of possible values for each input. It's possible to use the `matrix` keyword to define more complex combinations of inputs.

For example, you can use it to run tests on multiple browsers, or to test against multiple versions of a dependency.

```yaml
matrix:
  os: [ubuntu-latest, windows-latest, macos-latest]
  node: [8, 10, 12]
  browser: [chrome, firefox, safari]
  dependency: [1.0, 2.0, 3.0]
```

Here, the matrix specifies that the workflow should run on three different operating systems (ubuntu-latest, windows-latest, and macos-latest), three different versions of Node.js (8, 10, and 12), three different browsers (chrome, firefox, safari) and three different versions of a dependency (1.0, 2.0, 3.0). This means that the workflow will run a total of 81 test combinations in parallel, rather than sequentially.

Using the `matrix` keyword in this way can greatly improve the reliability of your workflow, as it allows you to test against a wide range of inputs and identify any potential issues before they are released to production.

Another important aspect of the matrix is that its values are available and can be used in the steps of a job.

Finally, it's also worth noting that the matrix can be defined in multiple jobs, and it's also possible to use it in conjunction with `if` statements to conditionally run certain jobs based on the matrix values.

## Summary

In summary, the `strategy` and `matrix` keywords in GitHub Actions are powerful tools for implementing parallel workflows. These keywords allow you to define multiple combinations of inputs that should be run in parallel, greatly speeding up your workflow and increasing its reliability. By using them, you can easily implement parallel workflows in your own projects and take advantage of the many benefits that concurrency has to offer.

**Related repo:** [GitHub-Actions-Deep-Dive](https://github.com/christosgalano/GitHub-Actions-Deep-Dive)
