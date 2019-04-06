from flask import Flask,request,render_template,redirect,jsonify
import pymysql,os
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd
import time,re , Current_Movies

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
def detial(m_no):
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

'''#영화등록
@app.route('/form', methods=['GET'])
def formTest():
    return render_template('form.html')#form.html을 호출하겟다
'''

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
    Current_Movies.movieInsert()
    app.run(host='0.0.0.0',port=80,debug=True)
#host0.0.0.0은 외부에서도 접근가능, port는 기본 5000으로 바꾸고 싶으면 바꾸면됨