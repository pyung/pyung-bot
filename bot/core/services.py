from bot.core.response import ResponseHandler
from bot.messenger.user_profile import Profile


class UserProfile(object):
    pass


class MoodService(ResponseHandler):
    def __init__(self, data, recipient_id, **kwargs):
        super().__init__(recipient_id, **kwargs)
        self.recipient_id = recipient_id
        self.service = kwargs.get('service')
        self.data = data
        self.user = Profile.get_by_fb_ID(self.recipient_id)

    def get_response(self):
        if self.user_profile:
            return self.handle_normal_response(self.data)


