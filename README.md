# Slackbot Sanji (FoodieBot)

A bot for Slack that gathers information on local restaurants based on an area. Future additional features could be dine in options with recipes. 

### Requirements 
--- 
This library requires Python 3.6 and above. Third party imports are Zomato API, flask, slackclient, slackeventsapi. Slack Events API requires a request url. I used ngrock, which will provide an https link. When you restart the ngrock, make sure to go to the slack events api app settings to input a new link and reverify the link. Make sure to run ngrock on port 3000 which is the same as Python.

### Getting Started
---
Create a virtual environment.
```
virtualenv foodiebot
source foodiebot/bin/activate
```

Install all requirements.
```
pip3 install r- requirements.txt
```

Run bot and ngrock.
```
#for foodiebot.py
python3 foodiebot.py

#for separation of class
python3 app.py
```

### Workflow

* Slack App
    * OAuths, Permissions, Authenticity URLs, Event Subscriptions (What scopes should it have?)
    * Install App
* Virtual Environment
    * install requirements.txt
* foodiebot.py
    * create a function that takes in the message
    * make a class for bot and a main file
    * create a help command to show all it can do. Also, basic functionality in sanji.py. More complex features in its own classes.
* Put methods in cogs
* Bring selenium web driver into this to order cabo bobs


