from bot.messenger.send_api import PostBackMessages
import datetime
from bot.models import UserModel
from bot.messenger.user_profile import Profile


class PayloadConversationHandler:
    def __init__(self, **kwargs):
        self.recipient_id = kwargs.get('recipient_id')

    def handle_get_started(self, postback_payload):
        postbackmessages = PostBackMessages(self.recipient_id)
        if postback_payload == 'GET_STARTED_PAYLOAD':
            UserModel(facebook_id=self.recipient_id, created_on=datetime.datetime.now(),
                      last_seen=datetime.datetime.now(), username=Profile.get_user_details(self.recipient_id))\
                .create_user()
            return postbackmessages.handle_get_started()
