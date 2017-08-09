from config.extensions import db


class UserModel:
    def __init__(self, facebook_id, **kwargs):
        self.username = kwargs.get('username')
        self.facebook_id = facebook_id
        self.last_seen = kwargs.get('last_seen')
        self.created_on = kwargs.get('created_on')
        self.bio = kwargs.get('bio')

    def create_user(self):
        user = db.insert_one({'username': self.username,
                              'facebook_id': self.facebook_id,
                              'last_seen': self.last_seen,
                              'created_on': self.created_on,
                              'bio': self.bio})
        if user:
            return user
        return False

    @staticmethod
    def get_user_by_facebook_id(facebook_id):
        user = db.find_one({facebook_id: facebook_id})
        return user
