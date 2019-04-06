from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver as wd
import time,re

driver = wd.Chrome(executable_path='./chromedriver')

#영화목록 가지고오기

Show_movie_title = [] #영화제목
Show_movie_genre = [] #영화연령
Show_movie_img = []  #영화포스터
Show_movie_img_Processing =[] #영화포스터주소(가공후)
#movie_score = [] #영화평점
Show_movie_open = [] #영화오픈날짜
Show_movie_story = [] #영화줄거리

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
    movieGenres = soup.find_all('em',class_='ico_movie')    
    for movieGenre in movieGenres:
        if movieGenre.text == "독점":
            continue
        else:
            Show_movie_genre.append(movieGenre.text)
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


#리스트안에 영화제목이 들어가졌나 확인
print(len(Show_movie_title))

#리스트안에 영화연령이 들어가졌나 확인
print(Show_movie_genre)

#리스트안에 영화이미지가 들어가졌나 확인
print(len(Show_movie_img))

#리스트안에 영화개봉날짜 들어가졌나 확인
print(len(Show_movie_open))

#리스트안에 스토리 들어가졌나 확인
print(len(Show_movie_story))