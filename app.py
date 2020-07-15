import os
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from flask import Flask
import json
from sanji import Sanji

tokens = {}
with open('configs.json') as jsonData:
    tokens = json.load(jsonData);

#Slackeventadapter documentation = SlackEventAdapter(TOKEN, Endpoint="/slack/events")
slack_event_adapter = SlackEventAdapter(tokens.get("SLACK_SIGNING_SECRET"), "/slack/events")
#slackwebclient documentation = WebClient(TOKEN)
slack_web_client = WebClient(token=tokens.get("SLACK_BOT_TOKEN"))


#========MESSAGE EVENTS=======
# handle messages
@slack_event_adapter.on("message")
def getMessage(payload):
    event = payload["event"]
    channel = event["channel"]

    #initialize Sanji
    bot = Sanji(channel)
    message = bot.handleMessage()

    slack_web_client.chat_postMessage(message)


if __name__ == "__main__":
    slack_event_adapter.start(port=3000)



