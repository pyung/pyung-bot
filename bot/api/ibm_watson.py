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
        :return: (tone_id)
                 tone_id - Watson Tone ID

        """

        response = watson.tone(sentence)
        return response
        emotion_tone = response.get('document_tone', None).get('tone_categories', None)[0]
        tones = emotion_tone.get('tones')
        to_return = ''
        dict_list = []
        for tone_dict in tones:
            dict_list.append(tone_dict.get('score'))
            print(dict_list)
            tone_score = max(dict_list)
            print(tone_score)
            if tone_dict.get('score') == tone_score:
                to_return = tone_dict.get('tone_id')
        return to_return

