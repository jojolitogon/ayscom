#!/bin/bash
cut -d',' -f1,3 files/sales.csv
echo ""
awk -F',' '{print $1, $3}' files/sales.csv
echo ""
grep "Shoes" files/sales.csv