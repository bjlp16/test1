import mysql.connector
from mysql.connector import Error
class DB():
    def __init__(self, cnct):
        self.connection = cnct
    def linkinDB(self):
        try:
            # 連接 MySQL/MariaDB 資料庫
            self.connection = mysql.connector.connect(
                host='localhost',          # 主機名稱
                database='sparadisedb', # 資料庫名稱
                user='root',        # 帳號
                password='1qaz2wsx')  # 密碼

            if self.connection.is_connected():
                # 顯示資料庫版本
                db_Info = self.connection.get_server_info()
                print("資料庫版本：", db_Info)
        except Error as e:
            print("資料庫連接失敗：", e)

#db = DB(None)
#db.linkinDB()