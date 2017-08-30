# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import random


class Config:
    """Base configuration."""
    APP_NAME = 'PyungBot'
    SECRET_KEY = os.environ.get('NORMAN_SECRET', 'a9fb1b64-1f0f-11e7-95e2-7077816bf77d')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    __version__ = '1.0'


class SlackConfig:
    pass


class ProdConfig:
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    BASE_URL = 'unit9-moodbot.herokuapp.com/'


class DevConfig:
    ENV = 'dev'
    DEBUG = True
    BASE_URL = "htpps://localhost:5000/"


class TestConfig:
    """Test configuration."""

    TESTING = True
    DEBUG = True
    BASE_URL = "htpps://localhost:5000/"


class MessageConfig:
    FAILURE_MESSAGE_TEMPLATE = ["*scratch my head* :(", "How do I respond to that... :O",
                                "I can be not-so-smart from time to time... :(",
                                "Err... you know I'm not human, right? :O", "I do not understand you.",
                                "Sorry I've got a little bit sick. BRB in 2 min :(",
                                "Oops... 404 My Witty Mind Not Found :O",
                                "Oops... My brain went MIA in the cloud, BRB in 2 :(",
                                "Hmm... How should I respond to that... :O"
                                ]

    RESPONSE_SEARCH_TEMPLATE = ["Sure, give me a few seconds... B-)", "Scanning the world... :D", "Zoom zoom zoom...",
                                "Going into the Food Cerebro... B-)",
                                "Believe me, I'm a foodie, not an engineer... B-)"]

    @classmethod
    def get_message_by_template(cls, template_name):
        template_name = cls.__dict__.get(template_name)
        random_response = random.choice(template_name)
        return random_response
