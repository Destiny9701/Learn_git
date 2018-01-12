# __author:"Destiny"
# date: 2018/1/9
import os
import sqlite3


class Userdata:
    CURRENT_PATH = os.path.split(os.path.abspath(__file__))[0]
    __DATABASE = os.path.join(CURRENT_PATH, "user.db")

    def __init__(self):
        conn = sqlite3.connect(Userdata.__DATABASE, check_same_thread=False)
        cursor = conn.cursor()  # os.path.exists()
        cursor.execute('''create table if not exists user(
        id              INTEGER PRIMARY KEY   autoincrement  ,\
        name            text                  not null,\
        password        text                  not null,\
        base_path       text                  not null,
        limit_disk      REAL                  DEFAULT 20000.00);\
        ''')
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def get_conn(cls):
        con = sqlite3.connect(Userdata.__DATABASE, check_same_thread=False)
        return con

    @staticmethod
    def check_name(name):
        conn = Userdata.get_conn()
        cursor = conn.cursor()
        cursor.execute('''select name from user where name = ?''', (name,))
        names = cursor.fetchall()
        cursor.close()
        conn.close()
        if names:
            return True
        else:
            return False
        pass

    @staticmethod
    def check_pwd_by_name(name, pwd):
        conn = Userdata.get_conn()
        cursor = conn.cursor()
        cursor.execute('''select password from user where name = ?''', (name,))
        password = cursor.fetchall()[0][0]
        cursor.close()
        conn.close()
        if pwd == password:
            return True
        else:
            return False
        pass

    def get_path_by_name(self, name):
        conn = Userdata.get_conn()
        cursor = conn.cursor()
        cursor.execute('''select base_path from user where name=?''', (name,))
        path = cursor.fetchall()[0][0]
        cursor.close()
        conn.close()
        return path

    @staticmethod
    def register(name, pwd, base_path):
        conn = Userdata.get_conn()
        cursor = conn.cursor()
        cursor.execute('''insert into user(name,password,base_path)
        values(?,?,?)''', (name, pwd, base_path))
        conn.commit()
        cursor.close()
        conn.close()
        pass

    @staticmethod
    def __test():
        conn = Userdata.get_conn()
        cursor = conn.cursor()
        cursor.execute('''insert into user(name,password,base_path)
        values('test','123456','hello path')''')
        conn.commit()
        cursor.execute('''select * from user''')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        for i in data:
            print(i)
        pass

    @classmethod
    def __test_data(cls):
        test_conn = Userdata.get_conn()
        test_cursor = test_conn.cursor()
        test_cursor.execute('''select * from user''')
        test_data = test_cursor.fetchall()
        test_cursor.close()
        test_conn.close()
        for i in test_data:
            print(i)


if __name__ == "__main__":
    # T = Userdata()
    # print(T.get_path_by_name("wangjian"))
    pass
