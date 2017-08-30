from bot.slack.send_api import Message
from bot.slack.user_profile import Profile
from config.base import MessageConfig


class ResponseHandler(Message):
    def __init__(self, recipient_id, **kwargs):
        super(ResponseHandler, self).__init__(recipient_id, **kwargs)
        self.user_details = self.user_profile.get_user_details(recipient_id)

    def bad_word_response(self):
        message_text = MessageConfig.BAD_WORD_TEMPLATE.replace('<username>', self.user_details['first_name'])
        return self.send_message("text", message_text=message_text)

    def handle_normal_response(self):
        message_text = MessageConfig.BAD_WORD_TEMPLATE
        return self.send_message("text", message_text=message_text)