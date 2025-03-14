"""
爬取页面,例如 0-1-100 从第0页开始到第一页，每页100张
"""

import time
import random
import undetected_chromedriver as uc #防cf检测浏览器对象
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login
import set_maxpage


url = "https://anime-pictures.net/posts?page={}&search_tag=girl&order_by=rating&ldate=4&lang=zh-cn"


class photos:
    def __init__(self,url,number,last_number,lodin_flag=0,start=0,end=1):#初始化
        self.number = number
        self.url = url
        self.start = start
        self.end = end
        self.last_number = last_number

        self.driver = uc.Chrome()  #driver_executable_path=r".\chromedriver.exe"
        self.wait = WebDriverWait(self.driver, 60, 0.2)
        self.driver.implicitly_wait(10)
        if login_flag == 1:
            username,password = input("输入账号密码(username-password):").split("-")
            login.login(driver=self.driver,username=username,password=password)
            time.sleep(random.uniform(2, 4))
            set_maxpage.set(driver=self.driver, number=self.number)

        time.sleep(random.uniform(2, 4))
        #运行隐藏参数js
        # self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': js})
    def page(self,count):
        #加载页面
        self.driver.get(self.url.format(count))
        # 等待页面加载
        print(f"________________________{count}________________________")
        time.sleep(random.uniform(1, 2))

    def all(self,last_number):
        for i in range(last_number,self.number+1):
            time.sleep(random.uniform(1,1.5))
            target = self.driver.find_element(By.XPATH,f"//*[@id=\"svelte\"]//span[{i}]/a/picture/img[@class=\"svelte-1ibbyvk\"]")
            time.sleep(random.uniform(1,1.6))
            empty = target.location_once_scrolled_into_view
            time.sleep(random.uniform(1, 1.6))
            target.click()
            time.sleep(random.uniform(1,1.8))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"svelte\"]/div/div[1]/div[1]//span[2]/a[@rel=\"external nofollow\"]")))
            target = self.driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]//span[2]/a[@rel=\"external nofollow\"]")
            empty = target.location_once_scrolled_into_view
            time.sleep(random.uniform(1,1.6))
            target.click()
            time.sleep(random.uniform(1, 1.9))
            self.driver.back()
            print(i,end=" ")
        print("")

    def run(self):

        for count in range(self.start,self.end):
            self.page(count)
            self.all(self.last_number)
            self.last_number = 1
        time.sleep(10)
        input("完毕！")
        self.driver.quit()



if __name__ == "__main__":
    end = 100
    login_flag = eval(input("是否注册(0:否,1:是):"))
    start, last_number, number = map(eval, input("上次页数-上次张数-每页张数:").split("-"))
    web_crawler = photos(url, number, last_number, login_flag, start, end)
    web_crawler.run()
    exit()

