#!/bin/bash
set -e
trap 'echo "Something went wrong. Exiting..."' ERR
echo "Starting ETL job..."
python3 etl_process.py
echo "ETL completed."