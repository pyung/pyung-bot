# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import hashlib
import json
from threading import Thread
from flask import jsonify, make_response
from functools import wraps
from datetime import date, datetime


from config.http_handler import base
from config.errors import HttpMethodError
from config.base import FBConfig


def async_task(f):
    """ Takes a function and runs it in a thread """
    @wraps(f)
    def _decorated(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return _decorated


def decode_data(data):
    return data.decode("utf-8")


def update_white_listed_domains():
    """https://graph.facebook.com/v2.6/me/messenger_profile?access_token=PAGE_ACCESS_TOKEN"""
    graph_api_url = FBConfig.GRAPH_API_URL.replace('messages', 'messenger_profile')
    data = {
        "setting_type": "domain_whitelisting",
        "whitelisted_domains": FBConfig.WHITE_LISTED_DOMAINS,
        "domain_action_type": "add"
            }
    try:
        request = base.exec_request('POST', graph_api_url, data=data)
        return request
    except HttpMethodError:
        return 'Error'


def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def generate_conversation_session(data):
    return hash_data(data)[:32]


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    raise TypeError("Type %s not serializable" % type(obj))


class Response:

    def __init__(self):
        self._response_ok = []
        self._response_error = []

    @staticmethod
    def response_ok(data):
        response = jsonify({'status': 'success', 'data': data}, 200)
        return make_response(response)


    @staticmethod
    def response_empty(data):
        response = jsonify({'status': 'success', 'data': data}, 204)
        return make_response(response)

    @staticmethod
    def response_error(message, error=None, error_code=None):
        response = json.dumps({'status': 'fail', 'message': message, 'error': error, 'error_code': error_code})
        return make_response(response, 400)

response = Response()


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