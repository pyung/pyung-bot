# -*- coding: utf-8 -*-
"""Factories to help in tests."""
import datetime

from factory import LazyFunction, Sequence
from factory.mongoengine import MongoEngineFactory
from config.extensions import db, session
from bot.models import UserModel


class BaseFactory(MongoEngineFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    facebook_id = Sequence(lambda n: '{0}'.format(n))
    last_seen = LazyFunction(datetime.datetime.now)
    created_at = LazyFunction(datetime.datetime.now)
    bio = Sequence(lambda n: '{0}'.format(n))
    active = True

    class Meta:
        """Factory configuration."""

        model = UserModel



