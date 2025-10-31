#!/bin/bash
URL=https://raw.githubusercontent.com/estelaromer/csv-examples/refs/heads/main/data.csv
DATE=$(date +%F)
FILENAME=sales_$DATE.csv

wget $URL -O $FILENAME
mkdir -p data/
mv $FILENAME data/
echo \"Data saved as data/$FILENAME\"