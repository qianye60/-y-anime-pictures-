import time
import random
from selenium.webdriver.common.by import By

def set(driver,number):
    time.sleep(random.uniform(1, 2))
    driver.get("https://anime-pictures.net/settings")
    time.sleep(random.uniform(1,2))
    input = driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]/div/div[2]/div[2]/table/tbody/tr[6]/td[2]/input")
    time.sleep(random.uniform(1, 2))
    input.clear()
    time.sleep(random.uniform(1, 2))
    input.send_keys(number)
    time.sleep(random.uniform(1,2))
    target = driver.find_element(By.XPATH,"//*[@id=\"svelte\"]/div/div[1]/div[1]/div/div[2]/div[2]/input")
    target.location_once_scrolled_into_view
    target.click()