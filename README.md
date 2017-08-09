# Unit9 Mood Bot
> A unit9 facebook bot that attempts to decipher mood from user messages.

![](bot.png)

- [Unit9 Mood Bot](#unit9-mood-bot)
- [How it works:](#how-it-works)
                - [Project Stack](#project-stack)
                - [Bot Details](#bot-details)
    - [Flask Integration Details:](#flask-integration-details)
                    - [Extensions](#extensions)
            - [Testing Bot:](#testing-bot)
            - [As a non-technical user](#as-a-non-technical-user)
            - [As a technical user](#as-a-technical-user)

# How it works:
    When the bot receives a message, it calls IBM_WATSON's tone_analyzer and tries to analyze the tone in the message.
    It passes this mood to it's message context which replies with the correct message for the mood sent.

##### Project Stack
    Language: Python3.5.2
    Framework: Flask
    CI: Travis CI and Bitbucker Pipelines
    Hosting: Heroku

##### Bot Details
    Name: unit9-moodbot
    page_url = ""
    short_url = ""



## Flask Integration Details:
######     Extensions
        Flask-Restful : For handling API requests
        FLask-WTF : For csrf_excemption during API requests.
        TinyMongo : Used as a replacement for the full fledge mongo instance       


#### Testing Bot:
####     As a non-technical user
         Go to "" and click on the "GET STARTED" button to check see the bot at work.
         You can also go to "www.messenger.com" and search for "unit9" and click on the bot icon that shows up.
         P.S: You need to sign in or sign up on facebook on either case.

####     As a technical user
         If you're looking to contribute to this project, go to "CONTRIBUTING.md" to read the contribution guidelines there.

         




 
