import os
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from flask import Flask
import json
from sanji import Sanji
# import zomatopy
import logging

#create logger, set level, set handler, set formatter
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

tokens = {}
with open('configs.json') as jsonData:
    tokens = json.load(jsonData)

app = Flask(__name__)

#Slackeventadapter documentation = SlackEventAdapter(TOKEN, Endpoint="/slack/events")
slack_event_adapter = SlackEventAdapter(tokens.get("SLACK_SIGNING_SECRET"), "/slack/events", app)
#slackwebclient documentation = WebClient(TOKEN)
slack_web_client = WebClient(token=tokens.get("SLACK_BOT_TOKEN"))
logger.warning(f"slackeventadapter {slack_event_adapter} and slackwebclient {slack_web_client}")

#========MESSAGE EVENTS=======
# handle messages
@slack_event_adapter.on("message")
def getMessage(payload):
    #is there a reason why event = payload["event"] doesn't work?
    #return {} if event does not exist
    event = payload["event"]
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    # #initialize Sanji
    if "food" in text.lower():
        bot = Sanji(channel_id)
        message = bot.handleMessage()
        response = slack_web_client.chat_postMessage(**message)

    if "austin" in text.lower():
        bot = Sanji(channel_id)
        message = bot.handleSuggestions()


if __name__ == "__main__":
    app.run(port=3000)



