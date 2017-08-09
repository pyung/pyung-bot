# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt
import pytest
from bot.models import UserModel

from .factories import UserFactory


@pytest.mark.usefixtures('db')
class TestUser:
    """UserModel tests."""

    def __int__(self):
        self.user = UserModel(username='foo', facebook_id='JFDBJFKJLNDSGG', last_seen=dt.datetime.now(),
                              bio='A user bio.')
        self.factory_user = UserFactory()

    def test_create_user(self):
        user = self.user.create_user()
        assert type(user) == dict

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        self.user.create_user()
        assert bool(self.user.created_on)
        assert isinstance(self.user.created_on, dt.datetime)

    def test_factory(self):
        """Test user factory."""
        assert bool(self.factory_user.username)
        assert bool(self.factory_user.email)
        assert bool(self.factory_user.created_at)

    def test_get_user_by_facebook_id(self):
        assert True if False else True

