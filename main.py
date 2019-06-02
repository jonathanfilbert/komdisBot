import tweepy
import random
import time


phrasesArray = []
CONSUMER_KEY = 0
CONSUMER_SECRET = 0
ACCESS_TOKEN = 0
ACCESS_TOKEN_SECRET = 0


def main():
    bot = authenticate()
    while True:
        phrase = pilihkata()
        bot.update_status(phrase.upper())
        delayEveryHour()


def authenticate():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


def delayEveryHour():
    time.sleep(5)


def pilihkata():
    file = open("phrases.txt")
    content = file.read()
    file.close()
    phrasesArray = content.split(",")
    return random.choice(phrasesArray)


if __name__ == "__main__":
    print(pilihkata().upper())
