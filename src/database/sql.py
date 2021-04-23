from sqlBaseConfig import *
import base64
class createDb:
    def create(self):
        CreateUserInfoTableSql = """
                   CREATE TABLE userInfo(
                    phone CHAR(11) PRIMARY KEY,
                    passwd VARCHAR(20) NOT NULL,
                    cookie LONGTEXT NOT NULL
        )
                """

        CreateGroupInfoTableSql = """
            CREATE TABLE groupinfo (
              groupId varchar(50) NOT NULL,
              groupName varchar(255) NOT NULL,
              PRIMARY KEY (groupId)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                """
        cursor.execute(CreateUserInfoTableSql)
        cursor.execute(CreateGroupInfoTableSql)

class  douBanDB:

    def DB_findARecord(self,phone):
        # 通过phone查询该组数据,查询到返回数据，查询不到返回None
        str(phone)
        findARecordSql = "SELECT * FROM userinfo  WHERE phone= %s"
        cursor.execute(findARecordSql, phone)
        res = cursor.fetchone()
        res =  list(res)
        res[2] = base64.b64decode(str(res[2]).encode("utf-8")).decode('utf-8')

        return res

    def DB_insertARecordToDb(self,phone, passwd=None, cookie=None):
        # 插入一组数据，（phone，passwd，cookie），成功True，失败False
        str(phone)
        str(passwd)
        str(cookie)
        cookies = base64.b64encode(str(cookie).encode("utf-8")).decode('utf-8')
        insertARecordToDb = "insert into userinfo values(%s,%s,%s)"
        try:
            aa=cursor.execute(insertARecordToDb, (phone, passwd, cookies))
            # print(aa)
            conn.commit()
            return True
        except:
            conn.rollback()
            return False

    def DB_deleteARecordToDb(self,phone):
        str(phone)
        deleteARecordSql = "DELETE FROM userinfo  WHERE phone= %s"
        try:
            cursor.execute(deleteARecordSql,phone)
            conn.commit()
            return True
        except:
            conn.rollback()
            return False

import json


# 使用base64的b64encode（）进行转码，转码之后在用‘utf-8’解码
# s 要转码的字符串



# cookieData= [{'domain': '.douban.com', 'expiry': 1681911052, 'httpOnly': False, 'name': '__utmv', 'path': '/', 'secure': False, 'value': '30149280.23614'}, {'domain': '.douban.com', 'expiry': 1621431052, 'httpOnly': False, 'name': 'push_doumail_num', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.douban.com', 'expiry': 1621431052, 'httpOnly': False, 'name': 'push_noty_num', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.douban.com', 'httpOnly': False, 'name': 'ck', 'path': '/', 'secure': False, 'value': '8LZk'}, {'domain': '.douban.com', 'expiry': 1618839632, 'httpOnly': False, 'name': '__utmt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.douban.com', 'expiry': 1618840852, 'httpOnly': False, 'name': '__utmb', 'path': '/', 'secure': False, 'value': '30149280.4.9.1618839033'}, {'domain': 'www.douban.com', 'expiry': 1681911052, 'httpOnly': False, 'name': '_pk_id.100001.8cb4', 'path': '/', 'secure': False, 'value': '8e3bcfa824ad4840.1618839031.1.1618839052.1618839031.'}, {'domain': '.douban.com', 'expiry': 1634607052, 'httpOnly': False, 'name': '__utmz', 'path': '/', 'secure': False, 'value': '30149280.1618839033.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}, {'domain': '.douban.com', 'expiry': 1621431051, 'httpOnly': True, 'name': 'dbcl2', 'path': '/', 'secure': False, 'value': '"236146471:1s6wOz9tVd4"'}, {'domain': '.douban.com', 'httpOnly': False, 'name': '__utmc', 'path': '/', 'secure': False, 'value': '30149280'}, {'domain': '.douban.com', 'expiry': 1681911052, 'httpOnly': False, 'name': '__utma', 'path': '/', 'secure': False, 'value': '30149280.310887542.1618839033.1618839033.1618839033.1'}, {'domain': '.douban.com', 'expiry': 1618846228, 'httpOnly': False, 'name': 'ap_v', 'path': '/', 'secure': False, 'value': '0,6.0'}, {'domain': '.douban.com', 'expiry': 1652535034, 'httpOnly': False, 'name': '__gads', 'path': '/', 'secure': False, 'value': 'ID=4a9528ee03c3de25-22213a3377c7009c:T=1618839034:RT=1618839034:S=ALNI_MY04M-3tBqbsRTUkKe8AnJGvVVSug'}, {'domain': 'www.douban.com', 'expiry': 1650375032, 'httpOnly': False, 'name': '__yadk_uid', 'path': '/', 'secure': False, 'value': '82Q2KuXIpFil6mAGzQUfxoegh18rYwiK'}, {'domain': 'www.douban.com', 'expiry': 1618840852, 'httpOnly': False, 'name': '_pk_ses.100001.8cb4', 'path': '/', 'secure': False, 'value': '*'}, {'domain': '.douban.com', 'expiry': 4772439031, 'httpOnly': False, 'name': 'douban-fav-remind', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.douban.com', 'expiry': 1650375010, 'httpOnly': False, 'name': 'bid', 'path': '/', 'secure': False, 'value': 'sbURDwXEgU4'}]
# # print(cookieData)
#
#
# douBan=douBanDB()


# print(douBan.DB_insertARecordToDb('15159669885','123456',cookieData))














