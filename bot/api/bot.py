from flask import Blueprint
from flask import make_response
from flask import request
from flask_restful import Resource

from config.extensions import csrf_protect
from config.utils import response
from config.base import FBConfig
from bot.messenger.utils import get_request_type

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
        print(request)
        args = request.args
        print(request.args)
        if args.get('hub.mode') == 'subscribe' and args.get('hub.verify_token') == FBConfig.MESSENGER_VERIFICATION_TOKEN:
            return make_response(args.get('hub.challenge').strip("\n\""))
        else:
            return response.response_error('Failed validation. Make sure the validation tokens match', args)

    def post(self):
        print('I got to post')
        data = request.get_data()
        request_type = get_request_type(data)
        print(request_type)
        return response.response_ok('Got it')
