from bot.messenger.send_api import Message
from bot.messenger.user_profile import Profile
from config.base import MessageConfig


class ResponseHandler(Message, Profile):
    def __init__(self, recipient_id, **kwargs):
        super(ResponseHandler, self).__init__(recipient_id, **kwargs)
        self.user_details = self.user_profile.get_user_details(recipient_id)

        self.no_response_list = ["*scratch my head* :(", "How do I respond to that... :O",
                                 "I can be not-so-smart from time to time... :(",
                                 "Err... you know I'm not human, right? :O", "I do not understand you."]
        self.error = ["Sorry I've got a little bit sick. BRB in 2 min :(", "Oops... 404 My Witty Mind Not Found :O",
                      "Oops... My brain went MIA in the cloud, BRB in 2 :(",
                      "Hmm... How should I respond to that... :O"]

        self.looking_replies = ["Sure, give me a few seconds... B-)", "Scanning the world... :D", "Zoom zoom zoom...",
                                "Going into the Food Cerebro... B-)",
                                "Believe me, I'm a foodie, not an engineer... B-)"]

    def bad_word_response(self):
        message_text = MessageConfig.BAD_WORD_TEMPLATE.replace('<username>', self.user_details['first_name'])
        return self.send_message("text", message_text=message_text)

    def handle_normal_response(self, mood, registered=False):
        message_text = MessageConfig.get_message_by_mood(mood)
        return self.send_message("text", message_text=message_text)

    def handle_happiness_response(self, mood, registered=False):
        message_text = MessageConfig.get_message_by_mood(mood)
        return self.send_message("text", message_text=message_text)

    def handle_sadness_response(self, mood, registered=False):
        message_text = MessageConfig.get_message_by_mood(mood)
        return self.send_message("text", message_text=message_text)

    def handle_anger_response(self, mood, registered=False):
        message_text = MessageConfig.get_message_by_mood(mood)
        return self.send_message("text", message_text=message_text)

    def handle_disgust_response(self, mood, registered=False):
        message_text = MessageConfig.get_message_by_mood(mood)
        return self.send_message("text", message_text=message_text)









