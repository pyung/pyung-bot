from flask import Blueprint
from flask import make_response
from flask import request
from flask_restful import Resource

from bot.core.processor import Processor
from bot.core.response import ResponseHandler
from bot.messenger.payload_conversation import PayloadConversationHandler
from config.extensions import csrf_protect
from config.utils import response, decode_data
from config.base import FBConfig
from bot.messenger.utils import get_request_type, postback_events, messaging_events

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route('/webhook', methods=['GET', 'POST'])
@csrf_protect.exempt
def webhook():
    view_class = WebHook()
    if request.method == "GET":
        return view_class.get()
    else:
        return view_class.post()


class WebHook(Resource):
    def __init__(self):
        self.message = None
        self.response = None

    @staticmethod
    def get():
        args = request.args
        if args.get('hub.mode') == 'subscribe' and args.get('hub.verify_token') == FBConfig.MESSENGER_VERIFICATION_TOKEN:
            return make_response(args.get('hub.challenge').strip("\n\""))
        else:
            return response.response_error('Failed validation. Make sure the validation tokens match', args)

    def post(self):
        data = request.get_data()
        request_type = get_request_type(data)

        if request_type == 'postback':
            for recipient_id, postback_payload, referral_load in postback_events(data):
                if referral_load:
                    payloadhandler = PayloadConversationHandler(recipient_id=recipient_id)
                    return payloadhandler.handle_conversation(postback_payload)
            return response.response_ok('success')

        elif request_type == "message":
            for recipient_id, message in messaging_events(data):
                if not message:
                    return response.response_ok('Success')
                self.response = ResponseHandler(recipient_id)
                if message['type'] == 'text':
                    message = decode_data(message.get('data'))
                print("message: ", message)
                Processor(message, recipient_id).process()
            return response.response_ok('success')
        else:
            return response.response_ok('success')
