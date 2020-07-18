import os
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from flask import Flask
import json
from sanji import Sanji
import logging

#create logger, set level, set handler, set formatter
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
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
    logger.warning(event = payload.get("event", {}))
    # channel_id = event.get("channel")
    # user_id = event.get("user")
    # text = event.get("text")
    # print(text)
    # channel = event["channel"]
    # text = event["text"]

    # #initialize Sanji
    # bot = Sanji(channel)
    # message = bot.handleMessage()

    # slack_web_client.chat_postMessage(message)


if __name__ == "__main__":
    app.run(port=3000)



