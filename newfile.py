import mysql.connector
from mysql.connector import Error
class DB():
    def __init__(self, cnct):
        self.connection = cnct
    def linkinDB(self):
        try:
            # �s�� MySQL/MariaDB ��Ʈw
            self.connection = mysql.connector.connect(
                host='localhost',          # �D���W��
                database='sparadisedb', # ��Ʈw�W��
                user='root',        # �b��
                password='1qaz2wsx')  # �K�X

            if self.connection.is_connected():
                # ��ܸ�Ʈw����
                db_Info = self.connection.get_server_info()
                print("��Ʈw�����G", db_Info)
        except Error as e:
            print("��Ʈw�s�����ѡG", e)

#db = DB(None)
#db.linkinDB()