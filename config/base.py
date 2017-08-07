# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config:
    """Base configuration."""
    APP_NAME = 'MoodBot'
    SECRET_KEY = os.environ.get('NORMAN_SECRET', 'a9fb1b64-1f0f-11e7-95e2-7077816bf77d')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    __version__ = '1.0'


class FBConfig(Config):
    """
    The GRAPH_API_URL format is <base_url><version><action><fields>
    """
    FACEBOOK_SECRET_KEY = 'EAANthzhbVD4BADdYUZBg84ud5T6uzbvUzfwgZChMBkq5Wxx6uuXp0ia7lkFSXQlwmSXOi1fzxDBDgSfheDx11LW4ZCPTxkufy8LyG4hMnE7ZC49r4hU6zhxqnXz9kbQPdM6Ngatnalw8dRzkHTk59odLc8h7tKftVeLZCxZCG1py0OPpjq5JS3'
    GRAPH_API_VERSION = 'v2.6'
    GRAPH_API_URL = 'https://graph.facebook.com/{0}/me/messages?access_token={1}'.format(
        GRAPH_API_VERSION, FACEBOOK_SECRET_KEY)
    MESSENGER_VERIFICATION_TOKEN = "this_is_unit9"


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    BASE_URL = 'htpps://norman-bot.herokuapp.com/'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    BASE_URL = "htpps://localhost:5000/"


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True


class ErrorConfig(Config):
    INVALID_VER_ID_ERROR = "Invalid/Expired Verification ID"
    INVALID_ROUTE_ERROR = "Looks like you do not have access to this page."
    INVALID_LOGIN_ERROR = "Invalid Email or Password"
    INVALID_ID_ERROR = "The provided ID is invalid"
    UNABLE_TO_SET_PASSWORD_ERROR = "Unable to set the provided password"


class MessageConfig(Config):
    BAD_WORD_TEMPLATE = "Hello <username>, Unfortunately your last message contains words" \
                        " I find offensive. Please, desist " \
                        "from using such words."
    GET_STARTED_MESSAGE = "Hello <username>".format(Config.APP_NAME)

