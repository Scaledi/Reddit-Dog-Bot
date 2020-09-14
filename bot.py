# region: importing
import praw # pip install praw (not a default package)
import re
import pdb
import os

import json
import time
import config
import requests
from datetime import datetime
# endregion
# region: variables
footer = """

---

This is a stupid bot made by a stupid human who makes stupid mistakes. Report issues and send hate [HERE](https://github.com/Scaledi/Send-Dog-Pics-Reddit)
"""
# endregion
# region: login/debug
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
# endregion

subreddit = reddit.subreddit("bobdarobber") # The subs to respond in

for comment in subreddit.stream.comments():
    if comment.saved == False:
        if re.search("had a dog", comment.body, re.IGNORECASE): # Had a dog
            comment.save()
            comment.reply("Damn... really sorry to hear that." + footer)
            print("done")