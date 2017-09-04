# -*- coding: utf-8 -*-
import logging
from flask import Flask

from bot.api import bot
from config.extensions import csrf_protect, handler
from config.base import DevConfig
from config import commands


def create_app(config_object=DevConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    csrf_protect.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(bot.blueprint)
    return None


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)



