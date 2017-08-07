class MoodBotError(Exception):
    def __init__(self, message=None, http_status=None):
        super(MoodBotError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class AuthKeyError(MoodBotError):
    """
    Auth Key Not Provided
    """
    pass


class HttpMethodError(MoodBotError):
    pass


class DeadConversationError(MoodBotError):
    """
    Raised when a conversation is dead.
    """
    pass


class SendAPIError(MoodBotError):
    """

    """
    pass
