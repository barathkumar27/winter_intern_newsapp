import feedparser
from feedparser.api import parse
import requests
from newspaper import fulltext
from pymongo import MongoClient

# NLP
# location
# RSS 
# 5 newspaper and tamil =ok

mainUrl = ['https://timesofindia.indiatimes.com/rssfeeds/-2128838597.cms',
           'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
           'https://timesofindia.indiatimes.com/rssfeeds/296589292.cms',
           'https://economictimes.indiatimes.com/rssfeedsdefault.cms',
           'https://www.thehindubusinessline.com/feeder/default.rss',
           'https://www.thehindu.com/feeder/default.rss']

posts = []
for url in mainUrl:
    posts.extend(feedparser.parse(url).entries)


try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.database

# Created or Switched to collection names: my_gfg_collection
collection = db.feeder


for entry in posts:
    title = str(entry.title)
    if ('death' in title) | ('lockdown' in title) | ('Covid' in title) | ('students' in title):
        url = entry.links[0]
        url = url.href

        html = requests.get(url).text
        text = fulltext(html)
        n = {
            "headline": entry.title,
            "news_content": text,
            "links": url
        }
        id = collection.insert_one(n)


cursor = collection.find()
for record in cursor:
    print(record)
