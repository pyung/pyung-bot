from config.base import FBConfig
from config.http_handler import base
from config.errors import HttpMethodError


class ProfileAPI:
    # @Todo : Handle Delete URLs
    def __init__(self, field_name):
        self.field_uri = 'messenger_profile'
        self.field_name = field_name
        self.graphAPIURL = FBConfig.GRAPH_API_URL.replace('messages', self.field_uri).replace('?fields=[]', '')
        self.graphAPIURLGET = FBConfig.GRAPH_API_URL.replace('messages', self.field_uri).replace('[]', self.field_name)


class PersitentMenu(ProfileAPI):
    """
    Setting, Getting and Deleting Persistent Menu.
    Make sure you read and understand this very well for sending the data :
    https://developers.facebook.com/docs/messenger-platform/messenger-profile/persistent-menu
    """
    def __init__(self):
        super().__init__('persistent_menu')

    def set_menu(self, menu_data):
        """
        https://developers.facebook.com/docs/messenger-platform/messenger-profile/persistent-menu has a detailed documentation
        on the menu data and formats.
        :param menu_data:
        :return:
        """
        request = base.exec_request('POST', self.graphAPIURL, data=menu_data)
        if request:
            return request

    def get_menu(self):
        request = base.exec_request('GET', self.graphAPIURLGET)
        if request:
            return request

    def delete_menu(self):
        request = base.exec_request('DELETE', self.graphAPIURLGET)
        if request:
            return request


class GetStarted(ProfileAPI):
    """
    Setting, Getting and Deleting Persistent Menu.
    Make sure you read and understand this very well for sending the data:
    https://developers.facebook.com/docs/messenger-platform/messenger-profile/get-started-button
    """
    def __init__(self):
        super().__init__('get_started')

    def set_message(self, payload):
        request = base.exec_request('POST', self.graphAPIURL, data=payload)
        if request:
            print(request)
            return True
        else:
            raise HttpMethodError('Unable to complete request.')

    def get_message(self):
        request = base.exec_request('GET', self.graphAPIURLGET)
        if request:
            return request
        else:
            raise HttpMethodError('Unable to complete request.')

    def delete_message(self):
            request = base.exec_request('DELETE', self.graphAPIURLGET)
            if request:
                return request
            else:
                raise HttpMethodError('Unable to complete request.')


class GreetingText(ProfileAPI):
    """
    Setting, Getting and Deleting Get Greeting Text.
    Make sure you read and understand this very well for sending the data :
    https://developers.facebook.com/docs/messenger-platform/messenger-profile/greeting-text
    """
    def __init__(self):
        super().__init__('greeting')

    def set_text(self, payload):
        request = base.exec_request('POST', self.graphAPIURL, data=payload)
        if request:
            print(request)
        else:
            raise HttpMethodError('Unable to complete request.')

    def get_text(self):
        request = base.exec_request('GET', self.graphAPIURLGET)
        if request:
            return request
        else:
            raise HttpMethodError('Unable to complete request.')

    def delete_message(self):
        request = base.exec_request('DELETE', self.graphAPIURLGET)
        if request:
            return request
        else:
            raise HttpMethodError('Unable to complete request.')


class WhitelistDomain(ProfileAPI):
    def __init__(self):
        super().__init__('whitelisted_domains')

    def set_text(self, payload):
        request = base.exec_request('POST', self.graphAPIURL, data=payload)
        if request:
            print(request)
        else:
            raise HttpMethodError('Unable to complete request.')

    def get_text(self):
        request = base.exec_request('GET', self.graphAPIURLGET)
        if request:
            return request
        else:
            raise HttpMethodError('Unable to complete request.')

    def delete_message(self):
        request = base.exec_request('DELETE', self.graphAPIURLGET)
        if request:
            return request
        else:
            raise HttpMethodError('Unable to complete request.')


class AccountLinking(ProfileAPI):
    """
    Not sure if we need this now but let's just leave it here.
    """
    pass


class TargetAudience(ProfileAPI):
    """
    Not sure if we need this now but let's just leave it here.
    """
    pass

