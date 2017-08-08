from bot.messenger.utils import bad_word_filter, ongoing_conversation, fill_slot, parse_sentence,create_conversational_log
from bot.core.response import ResponseHandler
from bot.core.mood import Happiness, Sadness, Anger, Disgust, Fear


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
            current_mood = parse_sentence(self.sentence)
            return self.launch_mood_service(current_mood, last_mood)
        else:
            print('New')
            current_mood = parse_sentence(self.sentence)
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
        print('I got to launch mood.')
        print(current_mood)
        if current_mood == 'joy':
            print('I got to joy')
            return Happiness(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'disgust':
            print('I got to disgust')
            return Disgust(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'anger':
            print('I got to anger')
            return Anger(current_mood, last_mood, self.recipient_id).get_response()
        elif current_mood == 'fear':
            print('I got to fear')
            return Fear(current_mood, last_mood, self.recipient_id).get_response()
        return Sadness(current_mood, last_mood, self.recipient_id).get_response()


