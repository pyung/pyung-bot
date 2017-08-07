import requests

from config.errors import HttpMethodError


class BaseAPI(object):
    """

    """

    _content_type = "application/json"

    def __init__(self):
        pass

    def _json_parser(self, json_response):
        response = json_response.json()
        return response

    def exec_request(self, method, url, data=None):
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        payload = data if data else data
        request = method_map.get(method)

        if not request:
            raise HttpMethodError(
                "Request method not recognised or implemented")

        response = request(
            url=url, json=payload, verify=True)

        return response.content

base = BaseAPI()
