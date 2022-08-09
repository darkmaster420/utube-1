import os

class Config:

    BOT_TOKEN = os.environ["5552934227:AAFqyiRwBcNSKOCSfNiRxqyYcS3SlAqBlJY"]                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["2707184"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["1692a0d37fbadc1e52f41e11cd1d6929"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["328240198201-dbq28t362cdqaj55ic7veemq7led5ap1.apps.googleusercontent.com"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["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"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["1465388760"])                            # Bot owner's telegram id

    AUTH_USERS = [BOT_OWNER,573863737]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



