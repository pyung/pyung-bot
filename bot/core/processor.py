from bot.messenger.utils import bad_word_filter, ongoing_conversation, fill_slot, parse_sentence
from bot.core.response import ResponseHandler
from bot.core.services import MoodService


class Processor:
    """
    Handles everything conversation
    """

    def __init__(self, sentence, recipient_id):
        self.sentence = sentence
        self.recipient_id = recipient_id

    def process(self):

        if isinstance(self.sentence, str):
            if bad_word_filter(self.sentence):
                return ResponseHandler(self.recipient_id).bad_word_response()

        if ongoing_conversation(self.recipient_id):
            service, last_mood = fill_slot(self.recipient_id)
            return self.launch_service(service, last_mood)
        else:
            result = parse_sentence(self.sentence, self.recipient_id)
            return ResponseHandler(self.recipient_id).handle_normal_response(context=result)

    def launch_service(self, service, last_mood):
        """
        There's a service launcher so i can extend to support other things
        :param service:
        :param last_mood:
        :return:
        """
        if service == 'mood':
            return MoodService(last_mood).get_response()


