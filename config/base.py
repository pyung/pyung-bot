# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import random


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
    ]
    MESSENGER_VERIFICATION_TOKEN = "this_is_unit09"


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
    GET_STARTED_MESSAGE = "Hello <username>, My name is MoodBot. I am a mood bot."
    BAD_WORD_TEMPLATE = "Hello <username>, Unfortunately your last message contains words" \
                        " I find offensive. Please, desist " \
                        "from using such words."

    HAPPINESS_MESSAGE_TEMPLATE = ["Awesome. Looks like you're happy.",
                                  "I like it when you're happy. It makes me happy too."
                                  "A happy message from you. I like that."
                                  "So, what's making you happy?",
                                  "You sound happy today. Mind sharing the good news?",
                                  "When you're happy and I'm happy, the whole world would be a very happy place."
                                  ]
    SADNESS_MESSAGE_TEMPLATE = ["Why are you sad?",
                                "Cheer me. It's no fun being sad.",
                                "I have some remedies for curing sadness.",
                                "Would you like to talk about why you're sad?",
                                "I detect sadness. Does it have anything to do with me?",
                                ]

    ANGER_MESSAGE_TEMPLATE = ["Why are you angry buddy?",
                              "I detect anger. Did I say something wrong.",
                              "I eat when am angry. Would you like some food to eat?",
                              "Huh. Someone's angry.",
                              "Do you want to talk about why you're angry?"]

    DISGUST_MESSAGE_TEMPLATE = ["Disgust, huh. That's new.",
                                "What's disgusting?",
                                "I detect disgust. What's that?"]

    FEAR_MESSAGE_TEMPLATE = ["I can sense fear. What are you afraid of?",
                             "I fear the dark myself so it's perfectly fine to be scared.",
                             "I used to be scared once.",
                             "You've gotta learn to overcome your fear."]

    @classmethod
    def get_message_by_template(cls, template_name):
        template_name = cls.__dict__.get(template_name)
        random_response = random.choice(template_name)
        return random_response


class IBMWatsonConFIG():
    username = '374dbea2-89f3-472a-8d7f-dd3da77d121f'
    password = 'kGkekLd1RpCr'
    version = '2016-05-19'
