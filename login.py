import time
import random
from selenium.webdriver.common.by import By

def login(driver,username,password):
    driver.get("https://anime-pictures.net/login?lang=zh-cn")
    time.sleep(random.uniform(1,2))
    driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]/div/div/form/table/tbody/tr[1]/td[2]/input").send_keys(username)
    time.sleep(random.uniform(1,2))
    driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]/div/div/form/table/tbody/tr[2]/td[2]/input").send_keys(password)
    time.sleep(random.uniform(1,2))
    target = driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]/div/div/form/table/tbody/tr[3]/td[2]/input")
    target.click()
    time.sleep(random.uniform(1, 2))