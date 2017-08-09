from bot.messenger.utils import bad_word_filter, ongoing_conversation, fill_slot, parse_sentence,create_conversational_log
from bot.core.response import ResponseHandler
from bot.core.mood import Happiness, Sadness, Anger, Disgust, Fear, Moods


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
            last_mood = fill_slot(self.recipient_id)
            print('The last mood is', last_mood)
            current_mood = parse_sentence(self.sentence)
            print('The current mood is ', current_mood)
            return self.launch_mood_service(current_mood, last_mood)
        else:
            current_mood = parse_sentence(self.sentence)
            print('The current mood is', current_mood)
            create_conversational_log(self.recipient_id, current_mood)
            return self.launch_mood_service(current_mood, last_mood=None)

    def launch_mood_service(self, current_mood, last_mood=None):
        """
        There's a service launcher so i can extend to support other things
        :param current_mood:
        :param service:
        :param last_mood:
        :return:
        """
        print('Current Mood in Launch Mood is', current_mood)
        return ResponseHandler(self.recipient_id).bad_word_response()
        if current_mood == 'joy':
            return Happiness(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'disgust':
            return Disgust(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'anger':
            return Anger(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'fear':
            return Fear(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'sadness':
            return Sadness(current_mood, last_mood, self.recipient_id).get_response()


