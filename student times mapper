#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    author_id = line[3]
    added_at = line[8]
    if len(added_at) > 11:
       hour = int(added_at[11] + added_at[12])
       print author_id,"\t", hour
