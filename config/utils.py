# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import hashlib
import json
import os
import random
import string
import uuid
from threading import Thread
from time import time
from flask import current_app, url_for, flash,jsonify, make_response, redirect
from functools import wraps


from config.http_handler import base
from config.errors import HttpMethodError
from config.base import FBConfig


def async_task(f):
    """ Takes a function and runs it in a thread """
    @wraps(f)
    def _decorated(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return _decorated


def decode_data(data):
    return data.decode("utf-8")


def update_white_listed_domains():
    """https://graph.facebook.com/v2.6/me/messenger_profile?access_token=PAGE_ACCESS_TOKEN"""
    graph_api_url = FBConfig.GRAPH_API_URL.replace('messages', 'messenger_profile')
    data = {
        "setting_type": "domain_whitelisting",
        "whitelisted_domains": FBConfig.WHITE_LISTED_DOMAINS,
        "domain_action_type": "add"
            }
    try:
        request = base.exec_request('POST', graph_api_url, data=data)
        return request
    except HttpMethodError:
        return 'Error'


def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def generate_conversation_session(data):
    return hash_data(data)[:32]


class Response:

    def __init__(self):
        self._response_ok = []
        self._response_error = []

    @staticmethod
    def response_ok(data):
        response = jsonify({'status': 'success', 'data': data}, 200)
        return make_response(response)


    @staticmethod
    def response_empty(data):
        response = jsonify({'status': 'success', 'data': data}, 204)
        return make_response(response)

    @staticmethod
    def response_error(message, error=None, error_code=None):
        response = json.dumps({'status': 'fail', 'message': message, 'error': error, 'error_code': error_code})
        return make_response(response, 400)

response = Response()

