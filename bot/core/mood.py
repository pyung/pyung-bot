from bot.core.response import ResponseHandler
from bot.models import UserModel


class Moods(ResponseHandler):
    def __init__(self, recipient_id, current_mood, last_mood=None):
        super(ResponseHandler, self).__init__(recipient_id)
        self.recipient_id = recipient_id
        self.current_mood = current_mood
        self.last_mood = last_mood
        self.user = UserModel.get_user_by_facebook_id(self.recipient_id)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response()
        return self.handle_normal_response()


class Happiness(Moods):
    def __init__(self, current_mood,  recipient_id, last_mood=None):
        super(Happiness, self).__init__(recipient_id, current_mood,  last_mood)

    def get_response(self):
        if self.user_profile:
            return self.handle_happiness_response()
        return self.handle_happiness_response()


class Sadness(Moods):
    def __init__(self, current_mood,  recipient_id, last_mood=None):
        super(Sadness, self).__init__(recipient_id, current_mood,  last_mood)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response()
        return self.handle_sadness_response()


class Anger(Moods):
    def __init__(self, current_mood,  recipient_id, last_mood=None):
        super(Anger, self).__init__(recipient_id, current_mood,  last_mood)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response()
        return self.handle_anger_response()


class Disgust(Moods):
    def __init__(self, current_mood, recipient_id, last_mood=None):
        super(Disgust, self).__init__(recipient_id, current_mood, last_mood)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response()
        return self.handle_disgust_response()


class Fear(Moods):
    def __init__(self, current_mood, recipient_id, last_mood=None):
        super(Fear, self).__init__(recipient_id, current_mood, last_mood)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response()
        return self.handle_disgust_response()





