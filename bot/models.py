import datetime
from config.extensions import db
from mongoengine.fields import ObjectId


class UserModel(db.Document):
    username = db.StringField(required=False, max_length=200, min_length=3)
    facebook_id = db.StringField(max_length=200, min_length=3)
    last_seen = db.DateTimeField(default=datetime.datetime.now())
    bio = db.StringField(max_length=5000, min_length=3)


class DBAPI:
    def __init__(self):
        self.user_model = UserModel

    def create_user(self, **kwargs):
        user_details = self.user_model(**kwargs)
        user = user_details.save()
        if user:
            return True
        return False

    def get_user_by_mongo_id(self, mongo_id):
        user = self.user_model.objects.filter(id=ObjectId(mongo_id))
        if user:
            return True
        return False

    def get_user_by_facebook_id(self, facebook_id):
        user = self.user_model.objects.filter(facebook_id=ObjectId(facebook_id))
        if user:
            return True
        return False

    def get_all(self):
        return self.user_model.objects.all()

    def get_update_user(self, **kwargs):
        return self.user_model.objects.get(kwargs.get('match')).update(kwargs.get('update'))
