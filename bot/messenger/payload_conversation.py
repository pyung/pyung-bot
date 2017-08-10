import json
from bot.messenger.send_api import PostBackMessages
import datetime
from bot.models import UserModel
from bot.messenger.user_profile import Profile
from config.utils import json_serial


class PayloadConversationHandler:
    def __init__(self, **kwargs):
        self.recipient_id = kwargs.get('recipient_id')

    def handle_get_started(self, postback_payload):
        postbackmessages = PostBackMessages(self.recipient_id)
        if postback_payload == 'GET_STARTED_PAYLOAD':
            created_on = json.dumps(datetime.datetime.now(), default=json_serial)
            last_seen = json.dumps(datetime.datetime.now(), default=json_serial)
            UserModel(facebook_id=self.recipient_id, created_on=created_on,
                      last_seen=last_seen, username=Profile.get_user_details(self.recipient_id))\
                .create_user()
            return postbackmessages.handle_get_started()
