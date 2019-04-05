from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd
import time,re

#flask는 웹, request는 값전달,render_template는 html띄우기위함

app=Flask(__name__) #초기화해서 app에 주소값 넣음

#메인화면
@app.route('/moviemain')#주소임
def mainmovie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="select * from current_movie" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('main.html',movieList=result)

#상영예정영화
@app.route('/Future_movie')
def to_be_movie():
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="select * from movie_to_be_screened" 
            cursor.execute(sql)
            result=cursor.fetchall()
    finally:
        conn.close()
    return render_template('Future_movie.html',to_be_movieList=result)

#ajax검색
@app.route('/ajaxmain',methods=['POST'])#주소임
def searchmovie():
    text=request.form.get('text')
    stype=request.form.get('stype')
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            if stype == 'current_movie_title':
                sql="select * from current_movie where current_movie_title like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
            elif stype == 'current_movie_genre':
                sql="select * from current_movie where current_movie_genre like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
            else:
                sql="select * from current_movie where current_movie_open like %s"
                text='%'+text+'%'
                cursor.execute(sql,text)
                result=cursor.fetchall()# 다가져올떄
                print(result)
    finally:
        conn.close()
        return jsonify(result)
    
    


#영화상세
@app.route('/movie_detail/<m_no>')#주소임
def detail(m_no):
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from current_movie where m_no= %s;'
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄

            sql='select * from board where m_no= %s;'
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()
    return render_template('movie_detail.html', movieInfo=result, board=board)

#상영예정영화상세
@app.route('/show_movie_detail/<m_no>')#주소임
def show_movie_detail(m_no):
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from movie_to_be_screened where m_no= %s;'
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄

            sql='select * from board where m_no= %s;'
            cursor.execute(sql,(m_no))
            board=cursor.fetchall()
    finally:
        conn.close()
    return render_template('show_movie_detail.html', movieInfo=result, board=board)

'''#영화등록
@app.route('/form', methods=['GET'])
def formTest():
    return render_template('form.html')#form.html을 호출하겟다
'''
#현재영화등록
@app.route('/')
def formresult():
    
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
    
    #######상영예정 영화목록 가지고오기##############

    Show_movie_title = [] #상영예정 영화제목
    #Show_movie_genre = [] #상영예정 영화등급
    Show_movie_img = []  #상영예정 영화포스터
    Show_movie_img_Processing =[] #상영예정 영화포스터주소(가공후)
    #movie_score = [] #상영예정 영화평점
    Show_movie_open = [] #상영예정 영화오픈날짜
    Show_movie_story = [] #상영예정 영화줄거리

    #페이지에 있는 영화제목 출력
    for movie_page in range(1,6):
        #print("https://movie.daum.net/premovie/released?opt=reserve&page=",movie_page)    
        url = "https://movie.daum.net/premovie/scheduled?opt=reserve&page={}".format(movie_page)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html,'html.parser')
        
        #영화 타이틀 추출.
        movietitles = soup.find_all('a',class_='name_movie #title')
        
        for movietitle in movietitles:
            Show_movie_title.append(movietitle.text)
        
        #영화 연령 추출
        #movieGenres = soup.find_all('em',class_='ico_movie')    
        #for movieGenre in movieGenres:
            #if movieGenre.text == "독점":
                #continue
            #else:
                #Show_movie_genre.append(movieGenre.text)
        
        #영화 이미지 추출
        movieImgs = soup.select("div span img")
            
        for movieImg in movieImgs:
            Show_movie_img.append(movieImg['src'])

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
            Show_movie_open.append(movieOpen_cleand_final[0])

        movieStorys = soup.find_all('a' , class_="desc_movie #synop")
        for movieStory in movieStorys:
            movieStory_cleand = movieStory.text.strip()
            movieStroy_cleand_final = movieStory_cleand.replace("\n","")
            Show_movie_story.append(movieStroy_cleand_final)
    #영화이미지주소 가공
    for moviesoso in range(len(Show_movie_img)):
        Show_movie_img_Processing.append(Show_movie_img[moviesoso].replace("//img1.daumcdn.net/thumb/C236x340/?fname=","")) 

    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    for insert in range(len(Show_movie_title)):    
        try:
            with conn.cursor() as cursor:
                sql="insert into movie_to_be_screened(show_movie_title,show_movie_img,show_movie_open,show_movie_story) values(%s,%s,%s,%s);"
                cursor.execute(sql,(Show_movie_title[insert],Show_movie_img_Processing[insert],Show_movie_open[insert],Show_movie_story[insert]))
                conn.commit()
        finally:
            pass
    else:
        conn.close()
        return render_template('index.html')
    #리스트안에 영화제목이 들어가졌나 확인
    #print(Show_movie_title)

    #리스트안에 영화연령이 들어가졌나 확인
    #print(Show_movie_genre)

    #리스트안에 영화이미지가 들어가졌나 확인
    #print(Show_movie_img)

    #리스트안에 영화개봉날짜 들어가졌나 확인
    #print(Show_movie_open)

    #리스트안에 스토리 들어가졌나 확인
    #print(Show_movie_story[0])

    

#영화삭제하기
'''@app.route('/delete_movie/<m_no>',methods=['GET'])
def deleteform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="delete from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            conn.commit()
    finally:
        conn.close()

        return redirect('/moviemain')'''

#영화내용 수정하기
'''@app.route('/update_movie/<m_no>',methods=['GET'])
def updateform(m_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
 
    try:
        with conn.cursor() as cursor:
            
            sql="select * from movie where m_no= %s;"
            cursor.execute(sql,(m_no))
            result=cursor.fetchone() #하나만 가져올떄
    finally:
        conn.close()

        return render_template('update_movie.html',list=result)'''
#영화수정
'''@app.route('/update_movie',methods=['POST'])
def updateformp():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    no = request.form.get('no') 
    title = request.form.get('title') 
    mdir = request.form.get('mdir') 
    act = request.form.getlist('act') 
    grade = request.form.getlist('grade') 
    date = request.form.getlist('date') 
    content = request.form.get('content')
    img = request.files['img']
    dirname=os.path.dirname(__file__) + '/static/uploads/'+img.filename

    try:
        with conn.cursor() as cursor:
            sql="update movie set m_title=%s,m_dir=%s,m_act=%s,m_content=%s,m_grade=%s,m_img=%s,m_date=%s where m_no=%s;"
            cursor.execute(sql,(title,mdir,act,content,grade,img.filename,date,no))
            conn.commit()
    finally:
        img.save(dirname)
        conn.close()
    return redirect('/moviemain')'''

#게시판글쓰기
@app.route('/board_write/<m_no>',methods=['GET'])
def boardW(m_no):
    return render_template('board_write.html',m_no=m_no)#form.html을 호출하겟다

@app.route('/board_write/<m_no>',methods=['POST'])
def boardP(m_no):
    title = request.form.get('title') 
    writer = request.form.get('writer') 
    content = request.form.get('content') 
    good = request.form.get('good') 
    m_no = request.form.get('m_no') 
    conn=pymysql.connect(host='127.0.0.1',
    user='root',
    password='qwer1234',
    db='movie',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with conn.cursor() as cursor:
            sql="insert into board(b_title,writer,b_content,good,m_no,b_date) values(%s,%s,%s,%s,%s,SYSDATE());"
            cursor.execute(sql,(title,writer,content,good,m_no))
            conn.commit()
    finally:
        conn.close()
    return redirect('/movie_detail/'+m_no)

#글내용
@app.route('/board_content/<b_no>',methods=['GET'])
def boardC(b_no):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='qwer1234',db='movie',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql='select * from board where b_no = %s' 
            cursor.execute(sql,(b_no))
            result=cursor.fetchone()

    finally:
        conn.close()
    return render_template('board_content.html',list=result)

if __name__=="__main__": #파일내에서만 직접적으로 동작하게끔
    app.run(host='0.0.0.0',port=80,debug=True)
#host0.0.0.0은 외부에서도 접근가능, port는 기본 5000으로 바꾸고 싶으면 바꾸면됨