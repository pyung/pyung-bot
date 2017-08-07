from config.http_handler import base
from config.errors import HttpMethodError
from config.base import FBConfig
import json


class Profile:
    @staticmethod
    def get_user_details(user_id):
        """
            :param user_id: accepts page scope user id (PSID)
            :return: json representation of the profile
        """

        para = '?fields=first_name,last_name,profile_pic,locale,timezone,gender&'
        graph_api_url = FBConfig.GRAPH_API_URL.replace('me/messages?', (user_id + para))
        request = base.exec_request('GET', graph_api_url)
        if request:
            return json.loads(request.decode(encoding='UTF-8'))
        else:
            raise HttpMethodError('Unable to complete request.')
