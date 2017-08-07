from flask import Blueprint
from flask import make_response
from flask import request
from flask_restful import Resource

from bot.core.response import ResponseHandler
from bot.messenger.utils import get_request_type, postback_events, messaging_events
from bot.messenger.payload_conversation import PayloadConversationHandler
from bot.core.processor import Processor
from config.extensions import csrf_protect
from config.utils import response, decode_data

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
        verify_token = 'python_rocks'
        if args.get('hub.mode') == 'subscribe' and args.get('hub.verify_token') == verify_token:
            return make_response(args.get('hub.challenge').strip("\n\""))
        else:
            return response.response_error('Failed validation. Make sure the validation tokens match', args)

    def post(self):
        pass
