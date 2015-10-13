#!/usr/bin/python

import sys

oldAuthor = None # save the old author's id
hourList = [] # save the list of hours that an author makes posts

for line in sys.stdin:
    data = line.strip().split("\t")

    author, hour = data

    if oldAuthor and author!=oldAuthor:
       # if the author changes to a new author, determine the hours of highest frequency, print each of them out
       LstOfMostFreqHours = set([x for x in hourList if all([hourList.count(x)>=hourList.count(y) for y in hourList])])
       for i in LstOfMostFreqHours:
           print oldAuthor,'\t', i
       oldAuthor = author # set author to the new author
       hourList = []
    
    oldAuthor = author
    hourList.append(hour)

if oldAuthor != None:
   # for the last author, determine the hours of highest frequency, print each of them out
   LstOfMostFreqHours = set([x for x in hourList if all([hourList.count(x)>=hourList.count(y) for y in hourList])])
   for i in LstOfMostFreqHours:
       print oldAuthor, "\t", i
       
