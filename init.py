
from flask.helpers import get_debug_flag

from app import create_app
from config.base import ProdConfig, DevConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig


app = create_app(CONFIG)
