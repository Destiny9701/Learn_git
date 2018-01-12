# __author:"Destiny"
# date: 2018/1/12
import json
import os
import socketserver
import sys

from bin.User import user

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

online_user = []


class FtpServer(socketserver.BaseRequestHandler):
    def setup(self):
        self.__user = user.Login()

    def handle(self):
        print("%s连上了服务器!" % self.client_address[0])
        self.request.send("True".encode("utf-8"))
        cmd_json = self.request.recv(1024)
        cmd_json = json.loads(str(cmd_json, encoding="utf-8"))
        if cmd_json["cmd"] == "login":
            msg = self.login(cmd_json["name"], cmd_json["password"])
            msg = {"login": str(msg)}
            msg = json.dumps(msg)
            self.request.send(msg.encode("utf-8"))
        elif cmd_json["cmd"] == "register":
            msg = self.__user.new_user(cmd_json["name"], cmd_json["password"])
            if msg:
                msg = {"register": "success"}
            else:
                msg = {"register": "fail"}
            msg = json.dumps(msg)
            self.request.send(msg.encode("utf-8"))
        elif cmd_json["cmd"] == "logout":
            if cmd_json["name"] in online_user:
                msg = self.logout(cmd_json["name"])
                msg = {"msg": msg}
                msg = json.dumps(msg)
                self.request.send(msg.encode("utf-8"))


        pass

    def login(self, name, pwd):

        # print(online_user)
        if name in online_user:
            return True
        else:
            try:
                msg = self.__user.login(name, pwd)
                if msg:
                    online_user.append(name)
            except IndexError:
                msg = False
            return msg
        pass

    def logout(self, name):
        """

        :param name: str
        :return: bool
        """
        if name in online_user:
            online_user.pop(online_user.index(name))
            return True
        else:
            return False

    pass


if __name__ == "__main__":
    ftp_server = socketserver.ThreadingTCPServer(("192.168.1.101", 6000), FtpServer)
    ftp_server.serve_forever()
