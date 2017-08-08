from config.base import IBMWatsonConFIG
import json
from watson_developer_cloud import ToneAnalyzerV3


watson = ToneAnalyzerV3(
    username=IBMWatsonConFIG.username,
    password=IBMWatsonConFIG.password,
    version=IBMWatsonConFIG.version)

"""
{
  "document_tone": {
    "tone_categories": [
      {
        "category_name": "Emotion Tone",
        "tones": [
          {
            "tone_id": "anger",
            "tone_name": "Anger",
            "score": 0.0
          },
          {
            "tone_id": "disgust",
            "tone_name": "Disgust",
            "score": 0.0
          },
          {
            "tone_id": "fear",
            "tone_name": "Fear",
            "score": 0.0
          },
          {
            "tone_id": "joy",
            "tone_name": "Joy",
            "score": 1.0
          },
          {
            "tone_id": "sadness",
            "tone_name": "Sadness",
            "score": 0.0
          }
        ],
        "category_id": "emotion_tone"
      },
      {
        "category_name": "Language Tone",
        "tones": [
          {
            "tone_id": "analytical",
            "tone_name": "Analytical",
            "score": 0.0
          },
          {
            "tone_id": "confident",
            "tone_name": "Confident",
            "score": 0.0
          },
          {
            "tone_id": "tentative",
            "tone_name": "Tentative",
            "score": 0.0
          }
        ],
        "category_id": "language_tone"
      },
      {
        "category_name": "Social Tone",
        "tones": [
          {
            "tone_id": "openness_big5",
            "tone_name": "Openness",
            "score": 0.086951
          },
          {
            "tone_id": "conscientiousness_big5",
            "tone_name": "Conscientiousness",
            "score": 0.270278
          },
          {
            "tone_id": "extraversion_big5",
            "tone_name": "Extraversion",
            "score": 0.512273
          },
          {
            "tone_id": "agreeableness_big5",
            "tone_name": "Agreeableness",
            "score": 0.598685
          },
          {
            "tone_id": "emotional_range_big5",
            "tone_name": "Emotional Range",
            "score": 0.174635
          }
        ],
        "category_id": "social_tone"
      }
    ]
  }
}

"""


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

        response = watson.tone(sentence)
        print(response)
        print(response[0])
        tone_categories = response[0].get('tone_categories')[0]
        print(tone_categories)
        return response


