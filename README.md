# Toolhub

[![CodeFactor](https://www.codefactor.io/repository/github/bkmakerspace/toolhub/badge)](https://www.codefactor.io/repository/github/bkmakerspace/toolhub) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Build Status](https://travis-ci.com/bkmakerspace/toolhub.svg?branch=master)](https://travis-ci.com/bkmakerspace/toolhub)

A service for tool awareness and organization.

## Installation

Development support on Linux/Ubuntu/OSX Platforms
Development on Windwos requires Docker pre-installed & "Windows Sub-System for Linux" feature enabled through control panel --> programs & features --> Turn Windows features on/off --> check "windows sub System for Linux"

Run the setup script and follow the instructions.

```bash
./script/setup
````

Once the setup process has installed docker and the needed containers, simply start the containers
```bash
./script/start
```

You can now find the server running at `http://127.0.0.1:8001`.
