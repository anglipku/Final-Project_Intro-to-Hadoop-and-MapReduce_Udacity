#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    tag = line[2]
    
    tag_list = tag.strip().split(' ')
    for A_tag  in tag_list:
        print A_tag
