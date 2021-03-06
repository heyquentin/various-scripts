#! /usr/bin/python
import time
import feedparser
import os
from termcolor import colored

def parser(feedtitle, url, textColor):
    counter = 0
    listCount = 1
    print(colored(feedtitle, textColor))
    d = feedparser.parse(url)
    while (counter <=4):
        print(str(listCount) + ": " + d['entries'][counter]['title'])
        counter +=1
        listCount +=1
    time.sleep(30)
    counter = 0
    listCount = 1
    os.system('clear')

while True:
    try:
        parser('Reddit Vancouver', 'http://www.reddit.com/r/vancouver/new/.rss', 'green')
        parser('PC Sales', 'http://www.reddit.com/r/bapcsalescanada/new/.rss', 'red')
    except:
        print("Hey something went wrong. I'll try again in a sec")
        time.sleep(30)
        os.system('clear')
        continue
