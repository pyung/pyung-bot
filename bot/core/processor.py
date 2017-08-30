from bot.slack.utils import bad_word_filter, ongoing_conversation, update_user_mood, parse_sentence
from bot.core.response import ResponseHandler


class Processor:
    """
    Handles everything conversation
    """

    def __init__(self, sentence, recipient_id):
        self.sentence = sentence
        self.recipient_id = recipient_id

    def process(self):
        pass

    def launch_service(self):
        pass
