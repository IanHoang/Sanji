from slack import WebClient
from slackeventsapi import SlackEventAdapter
import json

tokens = {}
with open('configs.json') as jsonData:
    tokens = json.load(jsonData)

slack_event_adapter = SlackEventAdapter(tokens.get("slack_signing_secret"), "/slack/events")
slack_web_client = WebClient(tokens.get("slack_bot_token"))

#=======MESSAGE EVENTS=======
# handles messages 
@slack_event_adapter.on("message")
def handleMessage(payload):
    message = payload["event"]
    payloadChannel = message["channel"]

    txt = message.get("text")
    if "food" in txt.lower():
        slack_web_client.chat_postMessage(
            channel= payloadChannel,
            text = "Alright, alright, alright. I'm finding some for you right now. What are you in for?"
        )
   
#=======ERROR EVENTS=======
# handles errors
@slack_event_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

if __name__ == "__main__":
    slack_event_adapter.start(port=3000)
