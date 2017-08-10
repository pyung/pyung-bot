from flask import json

import io
import os
import yaml

from bot.api.ibm_watson import Agent
from config.utils import generate_conversation_session
from bot.models import UserModel

BAD_WORDS = {'4r5e','5h1t','5hit','a55','anal','anus','ar5e','arrse','arse','ass','ass-fucker','asses'
                            ,'assfucker','assfukka','asshole','assholes','asswhole','a_s_s','b!tch','b00bs',
                          'b17ch','b1tch','ballbag','balls','ballsack','bastard','beastial','beastiality',
                          'bellend','bestial','bestiality','bi+ch','biatch','bitch','bitcher','bitchers',
                          'bitches','bitchin','bitching','bloody','blow job','blowjob','blowjobs','boiolas',
                          'bollock','bollok','boner','boob','boobs','booobs','boooobs','booooobs','booooooobs',
                          'breasts','buceta','bugger','bum','bunny fucker','butt','butthole','buttmuch','buttplug',
                          'c0ck','c0cksucker','carpet muncher','cawk','chink','cipa','cl1t','clit','clitoris','clits'
                        ,'cnut','cock','cock-sucker','cockface','cockhead','cockmunch','cockmuncher','cocks','cocksuck '
                        ,'cocksucked ','cocksucker','cocksucking','cocksucks ','cocksuka','cocksukka','cok',
                          'cokmuncher','coksucka','coon','cox','crap','cum','cummer','cumming','cums','cumshot','cunilingus',
                          'cunillingus','cunnilingus','cunt','cuntlick ','cuntlicker ','cuntlicking ','cunts','cyalis','cyberfuc',
                          'cyberfuck ','cyberfucked ','cyberfucker','cyberfuckers','cyberfucking ','d1ck','damn','dick','dickhead',
                          'dildo','dildos','dink','dinks','dirsa','dlck','dog-fucker','doggin','dogging','donkeyribber','doosh',
                          'duche','dyke','ejaculate','ejaculated','ejaculates ','ejaculating ','ejaculatings','ejaculation','ejakulate',
                         'fu', 'f u','f u c k','f u c k e r','f4nny','fag','fagging','faggitt','faggot','faggs','fagot','fagots','fags',
                         'fanny','fannyflaps','fannyfucker','fanyy','fatass','fcuk','fcuker','fcuking','feck','fecker','felching',
                         'fellate','fellatio','fingerfuck ','fingerfucked ','fingerfucker ','fingerfuckers','fingerfucking ','fingerfucks ','fistfuck','fistfucked ','fistfucker ','fistfuckers ','fistfucking ','fistfuckings '
                        ,'fistfucks ','flange','fook','fooker','fuck','fucka','fucked','fucker','fuckers','fuckhead','fuckheads',
                          'fuckin','fucking','fuckings','fuckingshitmotherfucker','fuckme ','fucks','fuckwhit','fuckwit',
                          'fudge packer','fudgepacker','fuk','fuker','fukker','fukkin','fuks','fukwhit','fukwit','fux','fux0r',
                          'f_u_c_k','gangbang','gangbanged ','gangbangs ','gaylord','gaysex','goatse','God','god-dam','god-damned',
                          'goddamn','goddamned','hardcoresex ','hell','heshe','hoar','hoare','hoer','homo','hore','horniest','horny',
                          'hotsex','jack-off ','jackoff','jap','jerk-off ','jism','jiz ','jizm ','jizz','kawk','knob','knobead','knobed',
                          'knobend','knobhead','knobjocky','knobjokey','kock','kondum','kondums','kum','kummer','kumming','kums','kunilingus',
                          'l3i+ch','l3itch','labia','lmfao','lust','lusting','m0f0','m0fo','m45terbate','ma5terb8','ma5terbate','masochist','master-bate',
                          'masterb8','masterbat*','masterbat3','masterbate','masterbation','masterbations','masturbate',
                          'mo-fo','mof0','mofo','mothafuck','mothafucka','mothafuckas','mothafuckaz','mothafucked ','mothafucker','mothafuckers','mothafuckin','mothafucking ',
                          'mothafuckings','mothafucks','mother fucker','motherfuck','motherfucked','motherfucker','motherfuckers','motherfuckin','motherfucking','motherfuckings','motherfuckka','motherfucks','muff','mutha',
                          'muthafecker','muthafuckker','muther','mutherfucker','n1gga','n1gger','nazi','nigg3r','nigg4h','nigga','niggah','niggas','niggaz','nigger','niggers ','nob','nob jokey','nobhead','nobjocky','nobjokey','numbnuts','nutsack',
                          'orgasim ','orgasims ','orgasm','orgasms ','p0rn','pawn','pecker','penis',
                          'penisfucker','phonesex','phuck','phuk','phuked','phuking','phukked','phukking','phuks','phuq','pigfucker','pimpis','piss','pissed','pisser','pissers','pisses ','pissflaps','pissin ','pissing','pissoff ',
                          'poop','porn','porno','pornography','pornos','prick','pricks ','pron','pube','pusse','pussi','pussies','pussy','pussys ','rectum','retard','rimjaw','rimming','s hit','s.o.b.','sadist','schlong','screwing','scroat','scrote',
                          'scrotum','semen','sex','sh!+','sh!t','sh1t','shag','shagger','shaggin','shagging','shemale','shi+','shit','shitdick','shite','shited','shitey','shitfuck','shitfull','shithead','shiting','shitings','shits','shitted','shitter',
                          'shitters ','shitting','shittings','shitty ','skank','slut','sluts','smegma','smut','snatch','son-of-a-bitch','spac','spunk','s_h_i_t','t1tt1e5','t1tties','teets','teez','testical','testicle','tit','titfuck','tits','titt','tittie5',
                          'tittiefucker','titties','tittyfuck','tittywank','titwank','tosser','turd','tw4t','twat','twathead','twatty','twunt','twunter','v14gra','v1gra','vagina','viagra','vulva','w00se','wang','wank','wanker','wanky','whoar','whore','willies','willy','xrated','xxx'}


def bad_word_filter(sentence):
    sentence_tokens = sentence.lower().split(" ")
    if BAD_WORDS.intersection(set(sentence_tokens)):
        return True
    return False


def ongoing_conversation(recipient_id):
    user = UserModel(recipient_id).get_user_by_facebook_id()
    print(user)
    if user:
        return True
    return False


def update_user_mood(recipient_id, current_mood):
    print('THe user facebook detail is')
    print(UserModel(recipient_id).get_user_by_facebook_id())
    return UserModel(recipient_id).update_mood(current_mood)


def parse_sentence(sentence):
    watson_response = Agent.parse(sentence)
    return watson_response


def get_request_type(payload):
    data = json.loads(payload)
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

