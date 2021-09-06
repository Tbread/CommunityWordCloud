import requests
from bs4 import BeautifulSoup

import time

from konlpy.tag import Okt
from collections import Counter

okt = Okt()
# baseurl = "https://gall.dcinside.com/mgallery/board/lists"
#위는마갤아래는정갤
baseurl = "https://gall.dcinside.com/board/lists"
headers = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'},
]


j = 0
authorlist = []
caltime = 0

for i in range(1,46):
    start = time.time()
    params = {'id': 'tree', 'page': i}

    response = requests.get(baseurl, params=params, headers=headers[0])

    soup = BeautifulSoup(response.content,  'html.parser')

    crawl = soup.select('.gall_list > tbody > tr.ub-content.us-post')

    if i % 100 == 0:
        print(i,'페이지 걸린시간',caltime)
        caltime = 0
    for lists in crawl:
        author = lists.select_one('td.gall_writer.ub-writer').text.strip()
        if author != '운영자':
            if 'ㅇㅇ' not in author:
                authorlist.append(author)
                end = time.time()
                caltime = (caltime + end - start)

count = Counter(authorlist)
amchang_rank = count.most_common(50)
v = 0
for i in amchang_rank:
    v += 1
    name = i[0]
    times = i[1]
    print(v,'위',name,'님은 글을',times,'번 작성하셨습니다.')



