# Final-Project_Intro-to-Hadoop-and-MapReduce_Udacity

This is my solution to the final project of course "Intro to Hadoop and MapReduce" on Udacity.  There are 3 verbal questions and 4 coding questions.  In the coding questions, I use python to code the mapper and reducer that carry out specific tasks.  My solutions has met all specifications and passed the review.

All 4 coding questions are based on a Udacity discussion forum dataset, which records the text of question posts, comments, answers, tags, along with the author information and timing.  The coding questions are:

1. Student Times: find for each student what is the hour during which the student has posted the most posts

2. Average Length: process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post

3. Popular Tags: write a mapreduce program that would output top 10 tags, ordered by the number of questions they appear in

4. Study Groups: write a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
