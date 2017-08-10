from bot.messenger.utils import bad_word_filter, ongoing_conversation, update_user_mood, parse_sentence
from bot.core.response import ResponseHandler


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
        current_mood = parse_sentence(self.sentence)
        if ongoing_conversation(self.recipient_id):
            if self.sentence == "mood":
                print('The message is mood in ongoing')
                return ResponseHandler(self.recipient_id).handle_last_mood()
            update_user_mood(self.recipient_id, current_mood)
            return self.launch_mood_service(current_mood)
        else:
            if self.sentence == "mood":
                print('The message is mood in new')
                return ResponseHandler(self.recipient_id).handle_no_mood_response(new=True)
            update_user_mood(self.recipient_id, current_mood)
            return self.launch_mood_service(current_mood, last_mood=None)

    def launch_mood_service(self, current_mood, last_mood=None):
        """
        There's a service launcher so i can extend to support other things
        :param current_mood:
        :param service:
        :param last_mood:
        :return:
        """
        if current_mood == 'joy':
            return ResponseHandler(self.recipient_id).handle_happiness_response()
        elif current_mood == 'disgust':
            return ResponseHandler(self.recipient_id).handle_disgust_response()
        elif current_mood == 'anger':
            return ResponseHandler(self.recipient_id).handle_anger_response()
        elif current_mood == 'fear':
            return ResponseHandler(self.recipient_id).handle_fear_response()
        elif current_mood == 'sadness':
            return ResponseHandler(self.recipient_id).handle_sadness_response()
        return ResponseHandler(self.recipient_id).handle_no_mood_response()

