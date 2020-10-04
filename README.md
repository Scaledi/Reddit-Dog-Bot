# A reddit bot that asks people for dog pics

because who does not like dogs.

fill your details into `templateconfig.py` then rename the file to `config.py`

---

add new commands with

```python
        elif re.search("triggers", comment.body, re.IGNORECASE): # what it does
            comment.save()
            comment.reply("reply" + footer)
            print("done tInt")
```

## Deffenitions

**triggers**: what you want the bot to respond to.

`had (a|my) dog` this means it will respond to "had a dog" OR "had my dog". you can add others by following this regex syntax.

ie: `(walked|fed) (a|my) dog` would allow for "walked a dog", "fed a dog", "walked my dog", and "fed my dog".

**Reply**: what you want the bot to reply with.

test commands with https://regex101.com
