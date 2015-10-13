#!/usr/bin/python

import sys

oldTag = None # save the oldTag
oldTagCount = 0 # save the oldTag's Count
Top10Tag = [] # the list of top 10 tags
Top10TagCount = [] # the list of top 1 tags' counts

for line in sys.stdin:
    tag = line

    if oldTag and oldTag != tag:
       # check if the old tag's count beats the current 10th tag
       # if so, replace the current 10th tag, and its count, with those of the old tag 

       if len(Top10TagCount) == 10:        
          if oldTagCount > min(Top10TagCount) :
             Top10Tag[Top10TagCount.index(min(Top10TagCount))]=oldTag
             Top10TagCount[Top10TagCount.index(min(Top10TagCount))]=oldTagCount
       else:
          Top10Tag.append(oldTag)
          Top10TagCount.append(oldTagCount)

       oldTag = tag # set tag to the new one
       oldTagCount = 0

    oldTag = tag
    oldTagCount = oldTagCount+1


if oldTag != None:
   # for the last tag, print id, question length, avg answer length
   # check if the old tag's count beats the current 10th tag
   # if so, replace the current 10th tag, and its count, with those of the old tag  
   if oldTagCount > min(Top10TagCount) :
      Top10Tag[Top10TagCount.index(min(Top10TagCount))]=oldTag
      Top10TagCount[Top10TagCount.index(min(Top10TagCount))]=oldTagCount

# Sort the final top 10 list, and print out
for i in range(10):

    print Top10Tag[Top10TagCount.index(max(Top10TagCount))], "\t", max(Top10TagCount)

    del Top10Tag[Top10TagCount.index(max(Top10TagCount))]
    del Top10TagCount[Top10TagCount.index(max(Top10TagCount))]
