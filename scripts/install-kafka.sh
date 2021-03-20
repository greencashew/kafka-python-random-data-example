#!/bin/bash

export $(grep -v '^#' ../.env | xargs) &>/dev/null

KAFKA_VERSION=2.7.0
KAFKA_FILE=kafka_2.13-$KAFKA_VERSION

cd ../
INSTALL_DIR=$(pwd)

[[ -d "vendor" ]] || mkdir vendor
cd vendor || exit

if [[ -z "${KAFKA_HOME}" ]]; then
  wget https://apache.mirrors.tworzy.net/kafka/$KAFKA_VERSION/$KAFKA_FILE.tgz
  tar xvf $KAFKA_FILE.tgz || exit
  echo "KAFKA_HOME=$INSTALL_DIR/vendor/$KAFKA_FILE" >>"$INSTALL_DIR/.env"
  rm -f $KAFKA_FILE.tgz
  echo "KAFKA installed \$KAFKA_HOME saved to .env"
else
  echo "Skipping installation of Kafka. KAFKA_HOME already set up: $KAFKA_HOME"
fi
