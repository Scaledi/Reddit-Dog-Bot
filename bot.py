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
        if re.search("(had a dog)?(my dog died)?", comment.body, re.IGNORECASE): # Had a dog/my dog died
            comment.save()
            comment.reply("sorry for your loss :(. have any pictures? I would love to see your dog." + footer)
            print("done t0")
        elif re.search("(Has)?(Got)?(Fed)?(Feed)? (a)?(my)? dog", comment.body, re.IGNORECASE): # Has a dog
            comment.save()
            comment.reply("Cool! Send dog pics!" + footer)
            print("done t1")
        elif re.search("want a dog", comment.body, re.IGNORECASE): # want a dog
            comment.save()
            comment.reply("What type of dog do you want?... and... find any cute pictures of that breed?" + footer)
            print("done t2")
        elif re.search("ate a dog", comment.body, re.IGNORECASE): # ate a dog
            comment.save()
            comment.reply("What type of dog do you want?... and... find any cute pictures of that breed?" + footer)
            print("done a damn monster")

# Code Documentation
# comment.save is the method used to avoid responding to the same comments if the bot reboots.
# re.search("regex string", comment.body, re.IGNORECASE) = regex.search("regex string", incommentbody, ignoring case)