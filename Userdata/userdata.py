# __author:"Destiny"
# date: 2018/1/9
import sqlite3
import os


class Userdata:
    CURRENTPATH = os.path.split(os.path.abspath(__file__))[0]
    def get_conn(self):
        con=sqlite3.connect(os.path.join(Userdata.CURRENTPATH),"user.db")


if __name__ == "__main__":
    print(Userdata.CURRENTPATH)
    pass
