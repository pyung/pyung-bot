# Unit9 Mood Bot
> A unit9 facebook bot that attempts to decipher mood from user messages.

![](bot.png)

Features
--------

- Easy database integration with TinyMongo
- Flask-WTForms integration for csrf_excemption
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- Flask's Click CLI configured with simple commands
- Mood Detection using IBM_WATSON API
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

Screenshots
-----------

![alt text](https://bytebucket.org/OlamilekanResearch/unit-9-bot-release-1.0/raw/50c37072372b5954b243fb86ac3b5c9f48500c50/screenshots/Screenshot_20170809-164653.png?token=9fbaaaed47b233cd1dc6524689205aff7f85d30f)

![alt text](https://bytebucket.org/OlamilekanResearch/unit-9-bot-release-1.0/raw/50c37072372b5954b243fb86ac3b5c9f48500c50/screenshots/Screenshot_20170809-164506.png?token=a2eb9ac7adf318d57da2aa798a33ebb353664fd7 )

![alt text](https://bytebucket.org/OlamilekanResearch/unit-9-bot-release-1.0/raw/50c37072372b5954b243fb86ac3b5c9f48500c50/screenshots/Screenshot_20170809-164519.png?token=b60d508b544ed86b4ad20527389176a9679dc86f)

![alt text](https://bytebucket.org/OlamilekanResearch/unit-9-bot-release-1.0/raw/50c37072372b5954b243fb86ac3b5c9f48500c50/screenshots/Screenshot_20170809-164531.png?token=060719f8bfcacfdff4d8cb686e460f3fcd9d2c2d)


# How it works:
    When the bot receives a message, it calls IBM_WATSON's tone_analyzer and tries to analyze the tone in 
    the message.It parses this mood to it's message context which replies with the correct message for the mood
    sent.


##### Project Stack
| Field         | Value         | 
| ------------- |:-------------:|
| Name          | Python3.5.2   | 
| Page URL      | Flask         | 
| CD           | Bitbucket Pipelines|
|CI             | Codeship
| Hosting       |  Heroku       |



##### Bot Details
| Field         | Value         | 
| ------------- |:-------------:|
| Name          | unit9-bot     | 
| Page URL      |[Unit9](https://www.facebook.com/Unit9-1840472079615683)          | 
| Messenger URL |[MoodBot Messenger URL](https://www.messenger.com/t/1840472079615683)|
| Short URL     |               |


## Flask Integration Details:
######     Extensions
| Field         | Value         | 
| ------------- |:-------------:|
| Flask-Restful | unit9-bot     | 
| FLask-WTF     | For csrf_excemption during API requests.| 
| TinyMongo |Used as a replacement for the full fledge mongo instance |

#### Entry Point : **[init.py](https://bitbucket.org/OlamilekanResearch/unit-9-bot-release-1.0/src/84025942e48c9a7f10a695c4b693e580d481b0e7/init.py?at=master)**


# Testing Bot:
####     As a non-technical user
Go to [MoodBot Messenger URL](https://www.messenger.com/t/1840472079615683) and click on the GET STARTED" button to check see the bot at work.
         You can also go to Go to [messenger](www.messenger.com) and search for "unit9" and click on the bot icon that shows up.
         
### P.S: You need to sign in or sign up on facebook on either case`.




####     As a technical user
If you're looking to contribute to this project, go to [CONTRIBUTING](https://bitbucket.org/OlamilekanResearch/unit-9-bot-release-1.0/src/84025942e48c9a7f10a695c4b693e580d481b0e7/CONTRIBUTING.md?at=master&fileviewer=file-view-default) to read the contribution guidelines there.

         




 
