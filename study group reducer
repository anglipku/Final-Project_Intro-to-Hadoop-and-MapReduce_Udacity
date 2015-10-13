#!/usr/bin/python

import sys

oldQuestionNode = None # save the old question's node id

Student_IDs = [] # the list of question/answers/comment id's for a forum thread

for line in sys.stdin:
    data = line.strip().split("\t")

    post_id, post_type, author_id = data

    if oldQuestionNode and post_type[0] == "q": # i.e. it's a question
       # print the old question's node id, and the list of student id
       print oldQuestionNode, "\t", Student_IDs

       oldQuestionNode = post_id # set question node ID to that of the new question
       Student_IDs = [author_id]

    elif oldQuestionNode:
         Student_IDs.append(author_id)
    else:
         oldQuestionNode = post_id
         Student_IDs.append(author_id)

if oldQuestionNode != None:
   # for the last question, print question node id, and student IDs
   print oldQuestionNode, "\t", Student_IDs
