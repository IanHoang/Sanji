# Slackbot Sanji (FoodieBot)

A bot for Slack that gathers information on local restaurants based on an area. Future additional features could be dine in options with recipes. 

### Requirements 
--- 
This library requires Python 3.6 and above. It also requires Zomato API, flask, slackclient, slackeventsapi.

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

