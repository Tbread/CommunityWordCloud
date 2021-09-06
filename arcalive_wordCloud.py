import requests
from bs4 import BeautifulSoup

from wordcloud import WordCloud

import shutil

import sys

from konlpy.tag import Okt
from collections import Counter

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.dcinside
okt = Okt()

baseurl = "https://arca.live/b/cgame"
headers = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'},
]



sys.stdout = open('output/list.txt','w+', -1, 'utf-8')

for i in range(13,221):
    params = {'p': i}

    response = requests.get(baseurl, params=params, headers=headers[0])

    soup = BeautifulSoup(response.content,  'html.parser')

    crawl = soup.select('.vrow')
    for lists in crawl:
        title = lists.select_one('.title')
        if title is not None:
            print(title.text)


shutil.copyfile('output/list.txt','output/copies.txt')

f = open('output/copies.txt','r', -1, 'utf-8')

line = f.read()
f.close()
words = okt.nouns(line)
for i,v in enumerate(words):
    if len(v)<2:
        words.pop(i)

for word in words:
    if word == '새끼':
        words.remove('새끼')
    if word == '씨발':
        words.remove('씨발')
    if word == '원래':
        words.remove('원래')
    if word == '그냥':
        words.remove('그냥')
    if word == '오늘':
        words.remove('오늘')
    if word == '필독':
        words.remove('필독')
    if word == '진짜':
        words.remove('진짜')
    if word == '지금':
        words.remove('지금')
    if word == '뭐임':
        words.remove('뭐임')
    if word == '하나':
        words.remove('하나')
    if word == '내일':
        words.remove('내일')
    if word == '병신':
        words.remove('병신')
    if word == '이면':
        words.remove('이면')
    if word == '이번':
        words.remove('이번')
    if word == '시발':
        words.remove('시발')
    if word == '언제':
        words.remove('언제')
    if word == '요즘':
        words.remove('요즘')
    if word == '정도':
        words.remove('정도')
    if word == '왜':
        words.remove('왜')
    if word == '절대':
        words.remove('절대')
    if word == '존나':
        words.remove('존나')

#욕설 제거




count = Counter(words)
wc = WordCloud(font_path='malgun.ttf', background_color='white',width=800,height=400)
noun_list = count.most_common(80)
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('output/wc.png')

