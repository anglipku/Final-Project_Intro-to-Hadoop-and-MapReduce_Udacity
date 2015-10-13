#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    post_id = line[0]
    post_type = line[5]
    author_id = line[3]
    if post_id != "id":
       print post_id ,"\t", post_type, "\t", author_id 
