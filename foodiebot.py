from slack import WebClient
from slackeventsapi import SlackEventAdapter
import json
import zomatopy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logger.DEBUG)

formatter = logger.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('foodiebot.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

tokens = {}
with open('configs.json') as jsonData:
    tokens = json.load(jsonData)

slack_event_adapter = SlackEventAdapter(tokens.get("slack_signing_secret"), "/slack/events")
slack_web_client = WebClient(tokens.get("slack_bot_token"))
zomato = zomatopy.initialize_app(tokens.get("ZOMATO_TOKEN"))


#=======MESSAGE EVENTS=======
# handles messages 
@slack_event_adapter.on("message")
def handleMessage(payload):
    message = payload["event"]
    payloadChannel = message["channel"]

    txt = message.get("text")
    if "food" in txt.lower():
        city_collections = zomato.get_collections(278)
        logger.debug(city_collections)
        slack_web_client.chat_postMessage(
            channel= payloadChannel,
            text = "Alright, alright, alright. I'm finding some for you right now."
        )
   
#=======ERROR EVENTS=======
# handles errors
@slack_event_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

if __name__ == "__main__":
    slack_event_adapter.start(port=3000)
