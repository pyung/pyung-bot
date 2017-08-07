class NormanError(Exception):
    def __init__(self, message=None, http_status=None):
        super(NormanError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class AuthKeyError(NormanError):
    """
    Auth Key Not Provided
    """
    pass


class HttpMethodError(NormanError):
    pass


class DeadConversationError(NormanError):
    """
    Raised when a conversation is dead.
    """
    pass


class SendAPIError(NormanError):
    """

    """
    pass
