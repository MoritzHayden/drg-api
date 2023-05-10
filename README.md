# DRG API

<div align="center">

  [![Language](https://img.shields.io/badge/language-python-yellow.svg)](https://www.python.org)
  [![Python Version](https://img.shields.io/github/pipenv/locked/python-version/MoritzHayden/drg-api/main/src?label=python&color=orange)](./src/Pipfile)
  [![Code Size](https://img.shields.io/github/languages/code-size/MoritzHayden/drg-api?color=green)](https://drgapi.com/)
  [![License](https://img.shields.io/github/license/MoritzHayden/drg-api?color=darkred)](./LICENSE)

  [![CodeQL](https://github.com/MoritzHayden/drg-api/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/MoritzHayden/drg-api/actions/workflows/codeql.yml)
  [![Pylint](https://github.com/MoritzHayden/drg-api/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/MoritzHayden/drg-api/actions/workflows/pylint.yml)
  [![Issues](https://img.shields.io/github/issues/MoritzHayden/drg-api?color=informational)](https://github.com/MoritzHayden/drg-api/issues)
  [![Pull Requests](https://img.shields.io/github/issues-pr/MoritzHayden/drg-api?color=informational)](https://github.com/MoritzHayden/drg-api/pulls)

</div>

## Table of Contents

- [About](#about)
- [Documentation](#documentation)
- [Local Development](#local-development)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [Legal](#legal)

## About

DRG API is a free API which returns Deep Rock Galactic information and resources.

## Documentation

Documentation using the OpenAPI Specification (OAS) is made available at [drgapi.com](https://drgapi.com/).

## Local Development

In order to run DRG API locally, perform the following steps:

1. Install [Python 3](https://www.python.org/)
2. Clone this [repository](https://github.com/MoritzHayden/drg-api):
   ```bash
   git clone https://github.com/MoritzHayden/drg-api.git
   ```
3. Navigate to the root directory:
   ```bash
   cd drg-api
   ```
4. Execute the [run.sh](./src/scripts/run.sh) script with the `-i` and `-d` flags:
   ```bash
   ./src/scripts/run.sh -i -d
   ```
4. Navigate to [localhost:8080](http://localhost:8080/) in your browser

## Dependencies

Dependencies are automatically scanned and updated with [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates) on a weekly interval, as configured in [dependabot.yml](./.github/dependabot.yml). For questions about security, please reference the [Security Policy](./docs/SECURITY.md).

## Deployment

DRG API is automatically deployed to the [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform) whenever a push is made to the [main branch](https://github.com/MoritzHayden/drg-api/tree/main).

## Contributing

Contributions are welcome! If you found a bug or have a request, please open an [issue](https://github.com/MoritzHayden/drg-api/issues). If you would like to contribute changes, please [fork](https://github.com/MoritzHayden/drg-api/fork) this repository, open a [pull request](https://github.com/MoritzHayden/drg-api/pulls) with your changes, and link the PR with an [issue](https://github.com/MoritzHayden/drg-api/issues). All contributions must adhere to the [Code of Conduct](./docs/CODE-OF-CONDUCT.md). PRs must recieve codeowner approval before they will be merged.

## Disclaimer

Neither this project nor its contributors are associated with Deep Rock Galactic or Ghost Ship Games in any way whatsoever.

## Legal

- [Terms of Service](./docs/TERMS-OF-SERVICE.md)
- [Security Policy](./docs/SECURITY.md)
- [MIT License](./LICENSE)

<div align="center">

  <p>Copyright &copy; 2023 Hayden Moritz</p>

</div>
