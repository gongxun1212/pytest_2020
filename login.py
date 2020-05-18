from common.base import Base
from common.config import host

login_url = host+"/console"

class LoginPage(Base):
    loc_1 = ("id", "txUserId") #用户名
    loc_2 = ("id", "passwordId") #密码
    loc_3 = ("xpath", '//*[@id="loginSubmit"]') #登录按钮

    #判断元素
    loc4 = ("xpath", "/html/body/div[1]/div[2]/div/div[1]/span")

    def input_user(self,username):
        self.send(self.loc_1,username)

    def input_psw(self, psw):
        self.send(self.loc_2, psw)

    def click_button(self):
        self.click(self.loc_3)

    def login(self, username,psw):
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

    # def login(self, username="admin", password="520013"):
    #     '''登录'''
    #     self.driver.get(login_url)
    #     self.send(self.loc_1, username)
    #     self.send(self.loc_2, password)
    #     self.click_button()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get("http://192.168.3.122:8180/console/login.do")
    web.login("admin", "520013")