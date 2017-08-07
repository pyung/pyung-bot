from flask import json


def get_request_type(payload):
    data = json.loads(payload)
    # print(data["entry"][0]["messaging"])
    # print(data["entry"][0]["messaging"][0])

    """
        b'{"object":"page","entry":[{"id":"1151771338259557","time":1493254959665,"messaging":[{"recipient":{"id":"1151771338259557"},"timestamp":1493254959665,"sender":{"id":"1280106375410348"},"postback":{"payload":"NORMAN_GET_STARTED_PAYLOAD"}}]}]}'

    """

    """
        b'{"object":"page","entry":[{"id":"1151771338259557","time":1493256041898,"messaging":[{"sender":{"id":"1280106375410348"},"recipient":{"id":"1151771338259557"},"timestamp":1493255796750,"message":{"quick_reply":{"payload":"NORMAN_GET_STARTED_MEANING"},"mid":"mid.$cAARNdNu-e39h3kCADlbrPs3xkIv4","seq":6039,"text":"What does that mean?"}}]}]}'

    """

    if data["entry"][0]["messaging"][0].get('postback'):
        return "postback"

    elif "messaging" in data["entry"][0]["messaging"][0]:
        return "message"

    try:
        if data["entry"][0]["messaging"][0]['message']['quick_reply'].get('payload'):
            return "postback"
    except KeyError:
        return "message"


def postback_events(payload):
    global referral_load
    data = json.loads(payload)
    postbacks = data["entry"][0]["messaging"]
    referral_load = ''

    for event in postbacks:
        sender_id = event["sender"]["id"]
        if data["entry"][0]["messaging"][0].get('postback'):
            postback_payload = event["postback"]["payload"]
            try:
                referral_load = event["postback"]["referral"]['ref']
            except KeyError:
                    pass
        else:
            try:
                postback_payload = event["message"]["quick_reply"]["payload"]
            except KeyError:
                pass
        yield sender_id, postback_payload, referral_load


def messaging_events(payload):
    data = json.loads(payload)

    messaging_events = data["entry"][0]["messaging"]

    for event in messaging_events:
        sender_id = event["sender"]["id"]

        # Not a message
        if "message" not in event:
            yield sender_id, None

        if "message" in event and "text" in event["message"] and "quick_reply" not in event["message"]:
            data = event["message"]["text"].encode('unicode_escape')
            yield sender_id, {'type': 'text', 'data': data, 'message_id': event['message']['mid']}

        elif "attachments" in event["message"]:
            if "location" == event['message']['attachments'][0]["type"]:
                coordinates = event['message']['attachments'][
                    0]['payload']['coordinates']
                latitude = coordinates['lat']
                longitude = coordinates['long']

                yield sender_id, {'type': 'location', 'data': [latitude, longitude],
                                  'message_id': event['message']['mid']}

            elif "audio" == event['message']['attachments'][0]["type"]:
                audio_url = event['message'][
                    'attachments'][0]['payload']['url']
                yield sender_id, {'type': 'audio', 'data': audio_url, 'message_id': event['message']['mid']}

            else:
                yield sender_id, {'type': 'text', 'data': "I don't understand this",
                                  'message_id': event['message']['mid']}

        elif "quick_reply" in event["message"]:
            data = event["message"]["quick_reply"]["payload"]
            yield sender_id, {'type': 'quick_reply', 'data': data, 'message_id': event['message']['mid']}

        else:
            yield sender_id, {'type': 'text', 'data': "I don't understand this", 'message_id': event['message']['mid']}
