def get_event_type(payload):
    event = payload.get('event').get('type')
    return event


def get_event_details(event_type, payload):
    text = payload.get('event').get('text')
    sender_id = payload.get('event').get('user')
    if event_type == 'message':
        return text, sender_id

