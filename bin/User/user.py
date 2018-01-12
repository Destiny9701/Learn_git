# __author:"Destiny"
# date: 2018/1/9
import logging
import os
from multiprocessing import Manager

from bin.User import userdata


class Login:
    def __init__(self):
        self.database = userdata.Userdata()
        self.file_path = self.database.CURRENT_PATH
        logging.basicConfig(
            filemode="a",
            filename=os.path.join(self.file_path, "user.log"),
            level=logging.INFO,
            format="%(asctime)s  [Msg]:%(message)s [Line]:%(lineno)d"
        )
        pass

    def login(self, name, pwd):
        login_status = self.database.check_pwd_by_name(name, pwd)
        if login_status:
            print("%s登录成功!欢迎!" % name)
            log_msg = "%s登录成功!" % name
            logging.info(log_msg)
            return True
        else:
            print("%s登录失败!用户名或密码错误！请重新登录或者注册!" % name)
            log_msg = u"%s登录失败!用户名或密码错误！" % name
            logging.info(log_msg)
            return False
        pass

    def new_user(self, name, pwd):
        name_status = self.database.check_name(name)
        if name_status:
            print("用户名%s已经被注册了！请换个名称." % name)
            return False
            pass
        else:
            self.database.register(name, pwd, os.path.join(self.file_path, name))
            logging.info("注册了一个用户名：%s 密码：%s的账户" % (name, pwd))
            print("%s 注册成功!" % name)
            return True
        pass


if __name__ == "__main__":
    T = Login()
    T.new_user("wangjian", "123456")
    T.login("wangjian", "123456")
    pass
