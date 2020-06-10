from bs4 import BeautifulSoup as bs
from os import environ
import requests
import tweepy

API_KEY = environ['API_KEY']
API_KEY_SECRET = environ['API_KEY_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACESS_TOKEN_SECRET = environ['ACESS_TOKEN_SECRET']

oldList = []

def startApplication():

    newList = []

    URL = 'https://www.bccloop.com/'
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')
    mainPage = soup.find(id='comp-imz7yqgj')

    list = mainPage.text.split("\n")
    for el in list:
        if len(el) > 3:
            if el[1] == ':':
                newList.append(el)
            elif el[2] == ':':
                newList.append(el)

    return newList

    """#Pulls all the HTML from BCCLoop website mainpage and sets it to var mainPage
    URL = 'https://www.bccloop.com/'
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')
    mainPage = soup.find(id='comp-imz7yqgj')
    #Open mainPageText.txt and write mainPage.text to it
    with open('mainPageText.txt', 'w') as info: #THIS GETS THE MAIN PAGE FROM BCC AND WRITES IT INTO TXT
        info.write(mainPage.text)
        info.close()"""

def getOldLst():
    """#Pulls text from caddyTimes (old list)
    oldCaddyLst = []
    oldText = open('caddyTimes.txt', 'r')
    lines = oldText.readlines()
    for line in lines:
        oldCaddyLst.append(line)
        oldText.close()"""
    return oldCaddyLst

def getNewLst():
    #Reads mainText and puts every line into a mass list
    massText = []
    newText = open('mainPageText.txt', 'r')
    lines = newText.readlines()
    for line in lines:
        massText.append(line)

    #filters this list and adds each line that fits to a new list
    newCaddyLst = []
    for el in massText:
        if len(el) > 3:
            if el[1] == ':':
                newCaddyLst.append(el)
            elif el[2] == ':':
                newCaddyLst.append(el)
    return newCaddyLst


#tweet out the caddylst
def tweet(newCaddyLst):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # opens old schedule text and rewrites it as new schedule
    with open('caddyTimes.txt', 'w') as text:
        for el in newCaddyLst:
            text.write(el)

    #handles the tweeting of the new schedule
    tempTweet = ''
    tweets = []
    while len(newCaddyLst) != 0:
        if len(tempTweet) < 240:
            tempTweet += (newCaddyLst[0] + "\n")
            del newCaddyLst[0]
        elif len(tempTweet) > 240:
            tweets.append(tempTweet)
            tempTweet = ''
    tweets.append(tempTweet)
    tweets.reverse()
    for el in tweets:
        api.update_status(el)
