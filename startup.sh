#!/usr/bin/env bash

# This script is intended to ease the build and startup process by running
# all necessary commands subsequently after being called.

poetry build
APP_VERSION=$(poetry version -s) docker compose up --build