import logging 
from zomato_distribution_api.zomato_wrapper import Zomato

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
                "*Okay, I got you.* :wave: What you in for?"
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


    def handleMessage(self):
        return {
            "username": self.username,
            "channel": self.channel,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.INTRO_BLOCK
            ]
        }
        
    def handleSuggestions(self):
        logger.debug(self.zomato.get_city_id(city_name="Austin", state_name="Texas"))
        # return {
        #     "username": self.username,
        #     "channel": self.channel,
        #     "icon_emoji": self.icon_emoji,
        #     "blocks": [
        #         self.INTRO_BLOCK
        #     ]
        # }


