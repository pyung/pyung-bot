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
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns


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

Screenshots
-----------

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :target: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
    :alt: Home page


##### Bot Details
| Field         | Value         | 
| ------------- |:-------------:|
| Name          | unit9-bot     | 
| Page URL      | ""            | 
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

         




 
