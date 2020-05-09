#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import praw
import json

reddit= praw.Reddit(client_id='dkt9ONSKhwb4Zw',
                   client_secret='RtaSrzt9gxT6mjX4XNoGVxD341w',
                   username='nishigandha2131',
                   password='Rajendra1995@',
                   user_agent='web scrapper')
subreddit=reddit.subreddit('all')
search_reddit1=subreddit.search('student visa',limit=None)
search_reddit2=subreddit.search('study abroad',limit=None)
search_reddit2=subreddit.search('international student',limit=None)
python_data = {}
python_data['i']=[]
python_comments={}
python_comments['j']=[]
for submission in search_reddit1:
    python_data['i'].append('{ "subreddit":'+submission.subreddit.display_name+',"title":'+submission.subreddit.title+',description":'+submission.subreddit.description+', "count_comments":'+str(submission.num_comments)+'}')
    com1=submission.comments.replace_more()
    for a in submission.comments.list():
        python_comments['j'].append({"comments": a.body})

for submission1 in search_reddit2:
    python_data['i'].append('{ "subreddit":'+submission1.subreddit.display_name+',"title":'+submission1.subreddit.title+',description":'+submission1.subreddit.description+', "count_comments":'+str(submission1.num_comments)+'}')
    com2=submission1.comments.replace_more()
    for b in submission1.comments.list():
        python_comments['j'].append({"comments": b.body})

for submission2 in search_reddit2:
    python_data['i'].append('{ "subreddit":'+submission2.subreddit.display_name+',"title":'+submission2.subreddit.title+',description":'+submission2.subreddit.description+', "count_comments":'+str(submission2.num_comments)+'}')
    com3=submission2.comments.replace_more()
    for c in submission2.comments.list():
        python_comments['j'].append({"comments": c.body})

with open('/Users/nishigandha/Desktop/json1.json','w') as json_file:
    json_file=json.dump(python_data,json_file)
with open('/Users/nishigandha/Desktop/json2.json','w') as json_file1:
    json_file1=json.dump(python_comments,json_file1)


# In[ ]:




