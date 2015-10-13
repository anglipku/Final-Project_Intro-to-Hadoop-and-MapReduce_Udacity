#!/usr/bin/python

import sys

oldQuestionNode = None # save the old question's node id
oldQuestionLength = 0 # save the old question's length
AnsLengthList = [] # the list of the length of answers for a question

for line in sys.stdin:
    data = line.strip().split("\t")

    post_id, post_type, parent_id, post_length = data

    if oldQuestionNode and post_type[0] == "q": # i.e. it's a question
       # print the old question's node id, question length, avg answer length          
       if AnsLengthList == []:
          print oldQuestionNode,"\t",oldQuestionLength,"\t", 0
       else:
          print oldQuestionNode,"\t",oldQuestionLength,"\t", sum(AnsLengthList)/len(AnsLengthList)


       oldQuestionNode = post_id # set question node ID to that of the new question
       oldQuestionLength = float(post_length)
       AnsLengthList = []

    elif oldQuestionNode and post_type[0] == "a":
         AnsLengthList.append(float(post_length))
    else:
         oldQuestionNode = post_id
         oldQuestionLength =float(post_length)

if oldQuestionNode != None:
   # for the last question, print id, question length, avg answer length
   if AnsLengthList == []:
      print oldQuestionNode,"\t",oldQuestionLength,"\t", 0
   else:
      print oldQuestionNode,"\t",oldQuesitonLength,"\t", sum(AnsLengthList)/len(AnsLengthList)
