import os
import sys
import urllib.request,json, time
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import pymysql

tmrvl=[]

url="https://movie.naver.com/movie/running/current.nhn"
response = urllib.request.urlopen(url)

soup=BeautifulSoup(response,'html.parser')
table=soup.select('dt.tit a')
for result3 in table:
        mtitle=str(result3.string)
        mcode=str(result3.attrs['href'])
        i = str(re.findall('\d+', mcode)[0])
        tmcode=tuple([i])
        tmtitle=tuple([mtitle])
        tmrvl.append(tmtitle+tmcode)

conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

c=conn.cursor()

#마리아 db에 넣을댸는 ??가아니고 %s로 써야ㅚㅁ
sql="INSERT IGNORE INTO test(title,codem) VALUES(%s,%s)"

c.executemany(sql, tmrvl)
#c.execute(sql)

conn.commit()



conn.close()

