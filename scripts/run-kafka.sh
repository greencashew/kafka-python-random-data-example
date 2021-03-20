#!/bin/bash

export $(grep -v '^#' ../.env | xargs) &>/dev/null

if [ -z "$KAFKA_HOME" ]; then
  echo "Please set \$KAFKA_HOME env. At .env. If kafka missed use install.sh"
  exit
fi

"$KAFKA_HOME"/bin/kafka-server-start.sh "$KAFKA_HOME"/config/server.properties
