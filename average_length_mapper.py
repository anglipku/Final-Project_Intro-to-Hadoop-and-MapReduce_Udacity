#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    post_id = line[0]
    post_type = line[5]
    parent_id = line[6]
    post_length = len(line[4])
   
    if post_id != "id":
       print post_id ,"\t", post_type, "\t", parent_id, "\t", post_length 
