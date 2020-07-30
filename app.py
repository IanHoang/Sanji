#standard library imports (ordered alphabetically)
import json
import logging
import os

#related third party imports (ordered alphabetically)
from slackeventsapi import SlackEventAdapter
from flask import Flask
from slack import WebClient

#local application imports (ordered alphabetically)
from sanji import Sanji

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
def introduceBot(channel_id, user_id, text):
    bot = Sanji(channel_id)
    message = bot.interpretCall()
    slack_web_client.chat_postMessage(**message)

#show commandslist
def handleCommandList(channel_id, user_id, text):
    bot = Sanji(channel_id)
    message = bot.showCommandList()
    slack_web_client.chat_postMessage(**message)

def handleRecommendations(channel_id, user_id, text):
    bot = Sanji(channel_id)
    message = bot.handleRecommendations()


#========MESSAGE EVENTS=======
# handles specific incoming messages
@slack_event_adapter.on("message")
def handleMessage(payload):
    event = payload["event"]
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")


    if "sanji" in text.lower():
        introduceBot(channel_id, user_id, text)
        # findSuggestions(channel_id, user_id, text)

    if "commands" in text.lower():
        handleCommandList(channel_id, user_id, text)

    if "recommendations" in text.lower():
        handleRecommendations(channel_id, user_id, text)
    

if __name__ == "__main__":
    app.run(port=3000)



