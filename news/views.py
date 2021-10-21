from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news 

r = requests.get("https://timesofindia.indiatimes.com/briefs")
# r = requests.get("https://startupstash.com/indian-startups/")
# r = requests.get("http://10000startups.com/blog")
# r = requests.get("https://www.arcanys.com/blog/startup-blogs")
# r = requests.get("https://www.startupindia.gov.in/content/sih/en/bloglist")

soup = BeautifulSoup(r.content, 'html5lib')

headings = soup.find_all('a')


headings = headings[49:-13] # removing footers

news = []

for th in headings:
    news.append(th.text)

print(news)



#Getting news

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':news, 'ht_news': ht_news})