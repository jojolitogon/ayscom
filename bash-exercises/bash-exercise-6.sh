#!/bin/bash
cut -d',' -f1,3 csv/sales.csv
echo ""
awk -F',' '{print $1, $3}' csv/sales.csv
echo ""
grep "Shoes" csv/sales.csv