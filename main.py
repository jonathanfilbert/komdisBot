import tweepy
import random
import time


phrasesArray = []
phraseNumber = {}
CONSUMER_KEY = "5ws7032LGLKO9mdnkluJeu5mh"
CONSUMER_SECRET = "xppA3EA7BkdDQzM9JevjPnkLrsZAg1oHZOiI2cGuk7pJdMV1Zv"
ACCESS_TOKEN = "1135194910162731008-4hIellt4Mrz3un6upab5nLv6H3zNrn"
ACCESS_TOKEN_SECRET = "H0eey8L5Nawkq2LYwAByasiiQkEIf4im2zp7AJubwBvR4"


def main():
    bot = authenticate()
    while True:
        try:
            phrase = pilihkata()
            numberOfExclamationmarks = checkPhrase(phrase)
            bot.update_status(phrase.upper()+" "+numberOfExclamationmarks*"!")
            print(phraseNumber)
            print("SUDAH KE TWEET "+phrase)
            delayEveryHour()
        except tweepy.TweepError:
            continue


def authenticate():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api


def checkPhrase(phrase):
    if phrase not in phraseNumber:
        phraseNumber[phrase] = 0
    else:
        phraseNumber[phrase] += 1
    return phraseNumber[phrase]


def delayEveryHour():
    time.sleep(10)


def pilihkata():
    file = open("phrases.txt")
    content = file.read()
    file.close()
    phrasesArray = content.split(",")
    return random.choice(phrasesArray)


if __name__ == "__main__":
    main()
