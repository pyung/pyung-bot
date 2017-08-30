from flask import Blueprint, jsonify
from flask import request
from flask_restful import Resource

from config.extensions import csrf_protect
from bot.slack.funcs import get_event_details, get_event_type
from bot.api.logic import LogicHandler
from config.utils import response

blueprint = Blueprint('api', __name__, url_prefix='/api')

from slackclient import SlackClient

sc = SlackClient("6C9EzTEnseSYA4HnVcJ8XAiI")


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

    def get(self):
        pass

    def post(self):
        payload = request.get_json()
        print(payload)
        event_type = get_event_type(payload)
        print(event_type)
        for sender, payload in get_event_details(event_type, payload):
            if event_type == 'message':
                sc.api_call(
                    "im.open",
                    user=sender,
                    text="Hello from Python! :tada:"
                )
            return response.response_ok('success')
        return response.response_ok('success')


        #
        # elif request_type == "message":
        #     for recipient_id, message in messaging_events(data):
        #         if not message:
        #             return response.response_ok('Success')
        #         if message['type'] == 'text':
        #             message = decode_data(message.get('data'))
        #             Processor(message, recipient_id).process()
        #     return response.response_ok('success')
        # return response.response_ok('success')
