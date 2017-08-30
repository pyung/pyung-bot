from flask import Blueprint, jsonify
from flask import request
from flask_restful import Resource

from bot.core.processor import Processor
from bot.core.response import ResponseHandler
from bot.slack.payload_conversation import PayloadConversationHandler
from config.extensions import csrf_protect
from config.utils import response, decode_data
from config.base import FBConfig
from bot.slack.utils import get_request_type, postback_events, messaging_events

blueprint = Blueprint('api', __name__, url_prefix='/webhook')


@blueprint.route('', methods=['GET', 'POST'])
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

    def get(self):
        pass

    def post(self):
        print("I got to post")
        data = request.get_json()
        print(data)
        return jsonify({'r': data})
        request_type = get_request_type(data)
        if request_type == 'postback':
            for recipient_id, postback_payload, referral_load in postback_events(data):
                    payloadhandler = PayloadConversationHandler(recipient_id=recipient_id)
                    return payloadhandler.handle_get_started(postback_payload)
            return response.response_ok('success')

        elif request_type == "message":
            for recipient_id, message in messaging_events(data):
                if not message:
                    return response.response_ok('Success')
                if message['type'] == 'text':
                    message = decode_data(message.get('data'))
                    Processor(message, recipient_id).process()
            return response.response_ok('success')
        return response.response_ok('success')
