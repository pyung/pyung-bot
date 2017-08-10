from config.extensions import db


class UserModel:
    def __init__(self, facebook_id, **kwargs):
        self.facebook_details = kwargs.get('facebook_details')
        self.facebook_id = facebook_id
        self.last_seen = kwargs.get('last_seen')
        self.created_on = kwargs.get('created_on')
        self.last_mood = kwargs.get('last_mood')
        self.bio = kwargs.get('bio')

    def create_user(self):
        user = db.insert_one({'username': self.facebook_details,
                              'facebook_id': self.facebook_id,
                              'last_seen': self.last_seen,
                              'created_on': self.created_on,
                              'bio': self.bio})
        if user:
            return user
        return False

    def get_user_by_facebook_id(self):
        user = db.find_one({'facebook_id': self.facebook_id})
        print(user)
        return user

    def get_last_mood(self):
        user = self.get_user_by_facebook_id()
        print(user.last_mood)
        return user.last_mood

    def update_mood(self, last_mood):
        db.update_one({"facebook_id": self.facebook_id}, {"$set": {"last_mood": last_mood}})
