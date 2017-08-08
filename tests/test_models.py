# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt
import pytest
from bot.models import UserModel

from .factories import UserFactory


# @pytest.mark.usefixtures('db')
# class TestUser:
#     """UserModel tests."""
#
#     def __int__(self):
#         self.user = UserModel(username='foo', facebook_id='JFDBJFKJLNDSGG', last_seen=dt.datetime.now(),
#                               bio='A user bio.')
#         self.factory_user = UserFactory()
#
#     def get_user_by_mongo_id(self):
#         """Get user by ID."""
#         self.user.save()
#         retrieved = UserModel.get_by_id(self.user.id)
#         assert retrieved == self.user
#
#     def test_created_at_defaults_to_datetime(self):
#         """Test creation date."""
#         self.user.save()
#         assert bool(self.user.created_at)
#         assert isinstance(self.user.created_at, dt.datetime)
#
#     def test_factory(self):
#         """Test user factory."""
#         assert bool(self.factory_user.username)
#         assert bool(self.factory_user.email)
#         assert bool(self.factory_userz.created_at)
#
