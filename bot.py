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

This is a stupid bot made by a stupid human who makes stupid mistakes. Report issues and send hate [HERE](https://github.com/Scaledi/Reddit-Dog-Bot). if your looking for a deeper meaning, there is none. I just like dogs bro.

---

It's worth noting I(the bot) am currently rate limited by reddit. once I reach a unknown (small) karma threshold on our current sub it will be removed. more [HERE](https://www.reddit.com/r/help/wiki/faq#wiki_why_am_i_being_told_.22you.27re_doing_that_too_much....22)
"""

# endregion
subreddit = reddit.subreddit("aww+dogs+bobdarobber+DogPictures+Animals+Pets") # The subs to respond in (syntax ("sub+sub+sub") ie: ("dogs+dog+aww"))
# region: debug

# just debbugging stuff. you will want to keep this off, unless.
if config.test_online == True:
    testsubmission = reddit.submission(id=config.online_id)
    print("working...")
    now = datetime.now()
    currenttime = now.strftime("%D:%H:%M")
    testsubmission.reply("booted at " + currenttime)
    print("finished. staus=Ok")
# endregion
# region: extra config
def listcomments(): 
    if config.show_feed == True:
        print(comment.body)
        print("- " + str(comment.author))
        print(comment.subreddit)
        print("---")

def ifrated():
    if config.is_rated == True:
        time.sleep(600)
    else:
        time.sleep(1)
# endregion
# region: responding
try:
    for comment in subreddit.stream.comments():
        if comment.saved == False:
            listcomments()
            if re.search("((my|our) (dog|doggo|pet) (died|got killed)|(we|I) put (our|my) (dog|doggo|pet) to sleep)", comment.body, re.IGNORECASE): # Had a dog/my dog died
                comment.save()
                comment.reply("sorry for your loss :(. have any pictures? I would love to see your dog." + footer)
                print("done t0")
                ifrated()
            elif re.search("(has|have|got|fed|feed|walk|walked) (a|my) dog", comment.body, re.IGNORECASE): # Has a dog
                comment.save()
                comment.reply("Cool! Send dog pics!" + footer)
                print("done t1")
                ifrated()
            elif re.search("want a dog", comment.body, re.IGNORECASE): # want a dog
                comment.save()
                comment.reply("What type of dog do you want?... and... find any cute pictures of that breed?" + footer)
                print("done t2")
                ifrated()
            elif re.search("(ate|killed) (my|a) dog", comment.body, re.IGNORECASE): # ate a dog
                comment.save()
                comment.reply("Cursed." + footer)
                print("done a damn monster")
                ifrated()
except:
    print("rate limited by reddit.")
# Code Documentation
# comment.save is the method used to avoid responding to the same comments if the bot reboots.
# re.search("regex string", comment.body, re.IGNORECASE) = regex.search("regex string", incommentbody, ignoring case)

# endregion