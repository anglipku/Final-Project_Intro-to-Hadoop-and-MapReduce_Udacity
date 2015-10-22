#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    post_id = line[0]
    post_type = line[5]
    author_id = line[3]
    abs_parent_id = line[7]

    if post_id == "id":
       continue

    if post_type[0] == "q": # i.e. if the post is a "question" 
       print post_id ,"\t", author_id 

    if post_type[0] != "q": # i.e. if the post is an "answer" or "comment"
       print abs_parent_id, "\t", author_id 
