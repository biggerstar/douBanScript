import pymysql
#打开数据库连接

conn = pymysql.connect(user = "root",passwd = "1234",db = "douban")
cursor=conn.cursor()