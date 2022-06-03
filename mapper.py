#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # the data is messy, only read those having correct column count
    if len(columns) == 8: 
        try:
            countConditions = float(columns[5])
            print("%s\t%s\t%s" % (columns[4],countConditions,1))
        except ValueError:
            pass