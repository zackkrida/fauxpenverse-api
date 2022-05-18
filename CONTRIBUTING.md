# Contributing to fauxpenverse

Thank you for your interest in contributing to fauxpenverse! This document is a set of guidelines to help you contribute to this project.

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Project Documentation

Please consult the [README](./README.md) and [CODEBASE](./CODEBASE.md) files at the root of this repository.

### Bugs

If you find a bug, please open an issue in this repository describing the bug. You can file a bug [here](https://github.com/zackkrida/fauxpenverse-api/issues/new?template=bug_report.md). You will see a bug report template with the required information you should provide.

After that, don't forget to tag the issue with the "Bug" label.

### Proposing changes or new features

If you have an idea of a new feature or change to how the fauxpenverse API works, please [start a discussion](https://github.com/zackkrida/fauxpenverse-api/discussions/new?category=ideas) so we can discuss the possibility of that change or new feature being implemented and released in the future. This lets us come to an agreement about the proposed idea before any work is done.

### Pull requests

Before you start writing code, make sure there is an issue open. Pull requests without a link to an existing issue won't be merged.

If you want to get started contributing code to this project but don't know exactly what to work on, we compiled a good list of issues labeled as [`good first issue`](https://github.com/zackkrida/fauxpenverse-api/labels/good%20first%20issue) which are small in scope and not so complex to solve. There are also issues labeled as [`help wanted`](https://github.com/zackkrida/fauxpenverse-api/labels/help%20wanted) which can be a bit more complex but are good examples of things we are currently accepting help from the community.

Any code modifications will have to be accompanied by the appropriate unit tests. This will be checked and verified during code review. Once the Pull Request is opened, our CI server will run the unit test suite and run a code linter to verify that the code follows the coding guidelines.

## Running the tests

### How to Run API live integration tests

You can check the health of a live deployment of the API by running the live integration tests.

1. Change directory to `fauxpenverse_api`

```
cd fauxpenverse_api
```

1. Install all dependencies for fauxpenverse API

```
pipenv install
```

Note: The following non-Python libraries or binaries are transient dependencies which will also need to be present on your computer for the project to run and install as expected:

- `librdkafka`
- `exempi`
- `audiowaveform`

3. Launch a new shell session

```
pipenv shell
```

4. Run API live integration test

```
./test/run_test.sh
```

### How to Run Ingestion Server tests

You can ingest and index some dummy data using the Ingestion Server API.

1. Change directory to ingestion server

```
cd ingestion_server
```

2. Install all dependencies for Ingestion Server API

```
pipenv install
```

3. Launch a new shell session

```
pipenv shell
```

4. Run the integration tests

```
python3 test/integration_tests.py
```

## Questions or Thoughts?

Feel free to [join us on Slack](https://make.wordpress.org/chat/) and discuss the project with the engineers and community members on #fauxpenverse. We also use [GitHub discussions](https://github.com/zackkrida/fauxpenverse-api/discussions) for feature requests, troubleshooting, and other 'off-topic' conversations.
