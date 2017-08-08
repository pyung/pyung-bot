from config.extensions import db


class UserModel:
    def __init__(self, facebook_id, **kwargs):
        self.username = kwargs.get('username')
        self.facebook_id = facebook_id
        self.last_seen = kwargs.get('last_seen')
        self.bio = kwargs.get('bio')

    def create_user(self, **kwargs):
        user = db.insert_one(**kwargs)
        if user:
            return True
        return False

    @staticmethod
    def get_user_by_facebook_id(facebook_id):
        user = db.find_one({facebook_id: facebook_id})
        print(user)
        if user:
            return True
        return False
