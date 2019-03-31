import pymysql
connection=pymysql.connect(host='127.0.0.1',
                            user='root',
                            password='qwer1324',
                            db='member',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql='''
            insert into users values('gildong1','1234','길동',33,
            'gildong@gmail.com','부산시 남구','male','010-1234-1234');
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql='''
            select  * from users;
        '''
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
finally:
    connection.close()