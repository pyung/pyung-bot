from flask import Blueprint, jsonify
from flask import request
from flask_restful import Resource

from config.extensions import csrf_protect
from bot.slack.funcs import get_event_details, get_event_type
from bot.api.logic import LogicHandler
from config.utils import response

blueprint = Blueprint('api', __name__, url_prefix='/api')

from slacker import Slacker

from slackclient import SlackClient


@blueprint.route('/webhook', methods=['GET', 'POST'])
@csrf_protect.exempt
def webhook():
    view_class = WebHook()
    if request.method == "GET":
        print("Fuck")
        return view_class.get()
    else:
        return view_class.post()


class WebHook(Resource):
    def __init__(self):
        self.message = None
        self.response = None

    def get(self):
        return response.response_error("Method Not Implemented")

    def post(self):
        payload = request.get_json()
        event_type = get_event_type(payload)
        if event_type == 'message':
            text, sender = get_event_details(event_type, payload)
            print("#bot-test")
            slack_client = SlackClient("wpDK0ba0GTDQ0lMK8SvglqyK")
            print(slack_client.api_call("api.test"))
        return response.response_ok('success')
