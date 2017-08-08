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


class FBConfig:
    """
    The GRAPH_API_URL format is <base_url><version><action><fields>
    """
    FACEBOOK_SECRET_KEY = 'EAANthzhbVD4BADdYUZBg84ud5T6uzbvUzfwgZChMBkq5Wxx6uuXp0ia7lkFSXQlwmSXOi1fzxDBDgSfheDx11LW4ZCPTxkufy8LyG4hMnE7ZC49r4hU6zhxqnXz9kbQPdM6Ngatnalw8dRzkHTk59odLc8h7tKftVeLZCxZCG1py0OPpjq5JS3'
    GRAPH_API_VERSION = 'v2.6'
    GRAPH_API_URL = 'https://graph.facebook.com/{0}/me/messages?access_token={1}'.format(
        GRAPH_API_VERSION, FACEBOOK_SECRET_KEY)
    WHITE_LISTED_DOMAINS = [
        "https://wallpaperbrowse.com/media/images/pictures-14.jpg",
        "http://norman-bot.herokuapp.com/static/landing/images/norman-android.png"
    ]
    MESSENGER_VERIFICATION_TOKEN = "this_is_unit09"


class ProdConfig:
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    BASE_URL = 'htpps://norman-bot.herokuapp.com/'


class DevConfig:
    ENV = 'dev'
    DEBUG = True
    BASE_URL = "htpps://localhost:5000/"


class TestConfig:
    """Test configuration."""

    TESTING = True
    DEBUG = True


class MessageConfig:

    BAD_WORD_TEMPLATE = "Hello <username>, Unfortunately your last message contains words" \
                        " I find offensive. Please, desist " \
                        "from using such words."

    @classmethod
    def get_message_by_mood(cls, current_mood):
        message_dict = "You got to message mood."
        return message_dict
        # return [message for mood, message in message_dict.items() if current_mood == mood]


class IBMWatsonConFIG():
    username = '374dbea2-89f3-472a-8d7f-dd3da77d121f'
    password = 'kGkekLd1RpCr'
    version = '2016-05-19'
