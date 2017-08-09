from bot.messenger.send_api import Message
from bot.messenger.user_profile import Profile
from config.base import MessageConfig


class ResponseHandler(Message, Profile):
    def __init__(self, recipient_id, **kwargs):
        super(ResponseHandler, self).__init__(recipient_id, **kwargs)
        self.user_details = self.user_profile.get_user_details(recipient_id)

    def bad_word_response(self):
        message_text = MessageConfig.BAD_WORD_TEMPLATE.replace('<username>', self.user_details['first_name'])
        return self.send_message("text", message_text=message_text)

    def handle_normal_response(self):
        message_text = MessageConfig.BAD_WORD_TEMPLATE
        print(message_text)
        return self.send_message("text", message_text=message_text)

    # @Todo: I know I could have handled all of the functions below in the handle_normal_response method but I felt I
    # it'd be better in the long run if each function ever needs to fork out and do more than just return the static text
    # from the config

    def handle_no_mood_response(self):
        message_text = MessageConfig.get_message_by_template('NO_MOOD_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)

    def handle_happiness_response(self):
        message_text = MessageConfig.get_message_by_template('HAPPINESS_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)

    def handle_sadness_response(self):
        message_text = MessageConfig.get_message_by_template('SADNESS_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)

    def handle_anger_response(self):
        message_text = MessageConfig.get_message_by_template('ANGER_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)

    def handle_disgust_response(self):
        message_text = MessageConfig.get_message_by_template('DISGUST_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)

    def handle_fear_response(self):
        message_text = MessageConfig.get_message_by_template('FEAR_MESSAGE_TEMPLATE')
        print(message_text)
        return self.send_message("text", message_text=message_text)
