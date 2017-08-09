from bot.messenger.send_api import PostBackMessages


class PayloadConversationHandler:
    def __init__(self, **kwargs):
        self.recipient_id = kwargs.get('recipient_id')

    def handle_get_started(self, postback_payload):
        postbackmessages = PostBackMessages(self.recipient_id)
        if postback_payload == 'GET_STARTED_PAYLOAD':
            return postbackmessages.handle_get_started()
