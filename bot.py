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
# region: login
reddit = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "DogB0t By u/bobdarobber")
print("finished logging in")
# endregion
# region: variables
footer = """

---

This is a stupid bot made by a stupid human who makes stupid mistakes. Report issues and send hate [HERE](https://github.com/Scaledi/Reddit-Dog-Bot)
"""

# endregion
subreddit = reddit.subreddit("aww+dogs+bobdarobber") # The subs to respond in (syntax ("sub+sub+sub") ie: ("dogs+dog+aww"))
# region: debug

# just debbugging stuff. you will want to keep this off, unless.
if config.test_online == True:
    testsubmission = reddit.submission(id=config.online_id)
    print("working...")
    now = datetime.now()
    currenttime = now.strftime("%D:%H:%M")
    testsubmission.reply("booted at " + currenttime)
    print("finished. staus=Ok")

if config.show_feed == True:
    for comment in subreddit.stream.comments():
        print(comment.body)
        print("- " + str(comment.author))
        print(comment.subreddit)
        print("---")
# endregion
# region: responding
for comment in subreddit.stream.comments():
    if comment.saved == False:
        if re.search("(had a dog|my dog died)", comment.body, re.IGNORECASE): # Had a dog/my dog died
           comment.save()
           comment.reply("sorry for your loss :(. have any pictures? I would love to see your dog." + footer)
           print("done t0")
           time.sleep(600)
        elif re.search("(has|got|fed|feed|walk|walked) (a|my) dog", comment.body, re.IGNORECASE): # Has a dog
            comment.save()
            comment.reply("Cool! Send dog pics!" + footer)
            print("done t1")
            time.sleep(600)
        elif re.search("want a dog", comment.body, re.IGNORECASE): # want a dog
            comment.save()
            comment.reply("What type of dog do you want?... and... find any cute pictures of that breed?" + footer)
            print("done t2")
            time.sleep(600)
        elif re.search("(ate|killed) (my|a) dog", comment.body, re.IGNORECASE): # ate a dog
            comment.save()
            comment.reply("Cursed." + footer)
            print("done a damn monster")
            time.sleep(600)

# Code Documentation
# comment.save is the method used to avoid responding to the same comments if the bot reboots.
# re.search("regex string", comment.body, re.IGNORECASE) = regex.search("regex string", incommentbody, ignoring case)

# endregion

# region: except
# endregion