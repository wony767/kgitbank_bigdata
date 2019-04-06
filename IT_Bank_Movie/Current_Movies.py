from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd
import time,re

def movieInsert():
    #현재영화등록    
    driver = wd.Chrome(executable_path='./chromedriver')

    #영화목록 가지고오기

    movie_title = [] #영화제목
    movie_genre = [] #영화연령
    movie_img = []  #영화포스터
    movie_img_Processing =[] #영화포스터주소(가공후)
    #movie_score = [] #영화평점
    movie_open = [] #영화오픈날짜
    movie_story = [] #영화줄거리

    #페이지에 있는 영화제목 출력
    for movie_page in range(1,4):
        #print("https://movie.daum.net/premovie/released?opt=reserve&page=",movie_page)    
        url = "https://movie.daum.net/premovie/released?opt=reserve&page={}".format(movie_page)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')
        
        #영화 타이틀 추출.
        movietitles = soup.find_all('a',class_='name_movie #title')
        
        for movietitle in movietitles:
            movie_title.append(movietitle.text)
        
        #영화 연령 추출
        movieGenres = soup.find_all('em',class_='ico_movie')
        
        for movieGenre in movieGenres:
            if movieGenre.text == "독점":
                continue
            else:
                movie_genre.append(movieGenre.text)
        #영화 이미지 추출
        movieImgs = soup.select("div span img")
        
        for movieImg in movieImgs:
            movie_img.append(movieImg['src'])

        #영화 평점 추출
        #movieScores = soup.find_all('span',class_='num_grade')
        #for moiveScore in movieScores:
            #print(moiveScore.text)

        #영화개봉날짜 추출
        movieOpens = soup.find_all('span',class_='info_state')

        #영화개봉날짜 정규표현씩 활용하여 추출.
        for movieOpen in movieOpens:
            movieOpen_cleand = re.sub('[a-zA-Z]' , '', movieOpen.text)
            movieOpen_cleand = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                            '', movieOpen.text)              
            movieOpen_cleand_final = movieOpen_cleand.split()
            movie_open.append(movieOpen_cleand_final[0])
            movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        
        for movieStory in movieStorys:
            movieStory_cleand = movieStory.text.strip()
            movieStroy_cleand_final = movieStory_cleand.replace("\n","")
            movie_story.append(movieStroy_cleand_final)
    #영화이미지주소 가공
    for moviesoso in range(len(movie_img)):
        movie_img_Processing.append(movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 


    #리스트안에 영화제목이 들어가졌나 확인
    #print(len(movie_title))

    #리스트안에 영화연령이 들어가졌나 확인
    #print(len(movie_genre))

    #리스트안에 영화이미지가 들어가졌나 확인
    #print(movie_img)

    #리스트안에 영화개봉날짜 들어가졌나 확인
    #print(len(movie_open))

    #리스트안에 스토리 들어가졌나 확인
    #print(len(movie_story))

    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    for insert in range(len(movie_title)):    
        try:
            with conn.cursor() as cursor:
                sql="insert into current_movie(current_movie_title,current_movie_img,current_movie_genre,current_movie_open,current_movie_story) values(%s,%s,%s,%s,%s);"
                cursor.execute(sql,(movie_title[insert],movie_img_Processing[insert],movie_genre[insert],movie_open[insert],movie_story[insert]))
                conn.commit()
        finally:
            pass
    else:
        conn.close()
if __name__=="__main__":
    movieInsert()