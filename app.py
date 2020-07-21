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

#configure necessary tokens
tokens = {}
with open('configs.json') as jsonData:
    tokens = json.load(jsonData)

app = Flask(__name__)

#Slackeventadapter documentation = SlackEventAdapter(TOKEN, Endpoint="/slack/events")
slack_event_adapter = SlackEventAdapter(tokens.get("SLACK_SIGNING_SECRET"), "/slack/events", app)
#slackwebclient documentation = WebClient(TOKEN)
slack_web_client = WebClient(token=tokens.get("SLACK_BOT_TOKEN"))


#chat with bot
def converse(channel_id, user_id, text):
    bot = Sanji(channel_id)
    message = bot.interpretCall()
    slack_web_client.chat_postMessage(**message)

#show commandslist
def handleCommandList(channel_id, user_id, text):
    bot = Sanji(channel_id)
    message = bot.showCommandList()
    slack_web_client.chat_postMessage(**message)

#========MESSAGE EVENTS=======
# handle messages
@slack_event_adapter.on("message")
def handleMessage(payload):
    #is there a reason why event = payload["event"] doesn't work?
    #return {} if event does not exist
    event = payload["event"]
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    # #initialize Sanji
    if "sanji" in text.lower():
        converse(channel_id, user_id, text)
        # findSuggestions(channel_id, user_id, text)

    if "commands" in text.lower():
        handleCommandList(channel_id, user_id, text)
    

if __name__ == "__main__":
    app.run(port=3000)



