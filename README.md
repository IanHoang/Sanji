# Slackbot Sanji (FoodieBot)

A bot for Slack that gathers information on local restaurants based on an area. Future additional features could be dine in options with recipes. 

### Requirements 
--- 
This library requires Python 3.6 and above. It also requires Zomato API, flask, slackclient, slackeventsapi.

### Getting Started
---
Create a virtual environment
```
virtualenv foodiebot
source foodiebot/bin/activate
```

```
pip3 install r- requirements.txt
python3 bot.py
```
### Workflow

* Slack App
    * OAuths, Permissions, Authenticity URLs, Event Subscriptions (What scopes should it have?)
    * Install App
* Virtual Environment
    * install requirements.txt
* foodiebot.py
    * create a function that takes in the message
    * make it Object Oriented (Classify things) Started but should fix. It runs fine but has an error. Foodiebot.py works though.
* Put methods in cogs

