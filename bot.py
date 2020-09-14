import praw # pip install praw (not a default package)
import re
import pdb
import os

import json
import time
import config
import requests
from datetime import datetime

# Login
reddit = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "DogB0t By u/bobdarobber")
print("finished logging in")


# just debbugging stuff. you will want to keep this off, unless.
if config.test_online == True:
    testsubmission = reddit.submission(id=config.online_id)
    print("working...")
    now = datetime.now()
    currenttime = now.strftime("%D:%H:%M")
    testsubmission.reply("booted at " + currenttime)
    print("finished. staus=Ok")

subreddit = reddit.subreddit("bobdarobber")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("had (a)?(my)? dog", comment.body, re.IGNORECASE):
            comment.reply("Hi")
            print("done")