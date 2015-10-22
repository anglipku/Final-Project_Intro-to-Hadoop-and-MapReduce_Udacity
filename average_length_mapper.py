#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    post_id = line[0]
    post_type = line[5]
    abs_parent_id = line[7]
    post_length = len(line[4])
   
    if post_id == "id":
       continue

    if post_type[0] == "q": # i.e. if the post is a "question"
       print post_id ,"\t", "1", "\t", post_length # here, "1" indicates "question"

    if post_type[0] == "a": # i.e. if the post is an "answer"
       print abs_parent_id, "\t", "2", "\t", post_length
       # here "2" indicates "answer".  The double keys (id and "1", "2") will make sure that an answer always comes after the corresponding question
