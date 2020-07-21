import logging 
from zomato_distribution_api.zomato_wrapper import Zomato

#add logging functionality
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sanji.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Sanji:
    ''' FoodieBot class that contains all necessary functions '''

    INTRO_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "*Hello! I'm Sanji *, your personal food connoisseur. :wave: \n did you want some food recommendations?"
            )
        }
    }
    DIVIDER_BLOCK = {"type": "divider"}

    COMMANDS_LIST = {
        "type": "section", 
        "text": {
            "type": "mrkdwn",
            "text": (
                "*What can I do for ya?* :yum: \n *commands* = shows the commands list \n *food* = calls suggestions"
            )
        }
    }

    ZOMATO_CONFIG = {
        "user_key": "4f5dd962cca134ba8dbc59a89357b703"
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "Sanji"
        self.icon_emoji = ":robot_face:"
        self.zomato = Zomato("4f5dd962cca134ba8dbc59a89357b703")

    #handle first message
    def interpretCall(self):
        return {
            "username": self.username,
            "channel": self.channel,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.INTRO_BLOCK
            ]
        }
        
    #provide suggestions of places to eat
    def handleSuggestions(self):
        logger.debug(self.zomato.get_city_name(278))
        logger.debug(self.zomato.get_collections(278))
        print(self.zomato.get_collections(278))


    def showCommandList(self): 
        return {
            "username": self.username,
            "channel": self.channel,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.DIVIDER_BLOCK,
                self.COMMANDS_LIST,
                self.DIVIDER_BLOCK
            ]
        }



