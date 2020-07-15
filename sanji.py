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

    def __init__(self, channel):
        self.channel = channel
        self.username = "Sanji"
        self.icon_emoji = ":robot_face:"


    def handleMessage(self):
        # return {
        #     "channel" = self.channel,
        #     "username" = self.username,
        #     "icon_emoji" = self.icon_emoji,
        #     "blocks" = [
        #         self.INTRO_BLOCK
        #     ]
        # }
        message = "Hello there pal"
        return message

    def handleSuggestions(self):
        pass

