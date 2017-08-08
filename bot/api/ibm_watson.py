from config.base import IBM_WATSON_CONFIG
import json
from watson_developer_cloud import ToneAnalyzerV3


watson = ToneAnalyzerV3(
    username=IBM_WATSON_CONFIG.username,
    password=IBM_WATSON_CONFIG.password,
    version='2016-05-19')


class Agent:
    """
    An instance of our api.ai agent
    """
    @staticmethod
    def parse(sentence, session_id):
        """

        :param sentence: The sentence to parse (String)
        :param session_id: A unique identifier for each user
        :return: (serviceName, intentMatched, actionIncomplete, suggestedResponse)
                 service_name - this corresponds to the action specified under the intent matched
                 intent - this corresponds to the intent name on api.ai,
                 action_incomplete - (boolean) returns true if required slots are missing,
                 suggested_response - response filled on api.ai

        """
        print("querying api.ai, sentence = ", sentence)
        print(json.dumps(watson.tone_chat(sentence), indent=2))
        return watson.tone_chat(sentence)

