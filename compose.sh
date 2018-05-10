#!/usr/bin/env bash

if [ "${1}" == "dev" ]; then
  shift
  docker-compose -f docker-compose.dev.yml ${@}
else
  docker-compose ${@}
fi
