from selenium import webdriver
import time
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("http://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请尽快扫码登录")
        time.sleep(10)

def picking(method):
    # browser.get("https://www.taobao.com")
    # time.sleep(3)
    browser.find_element_by_id("q").send_keys("暖手宝")
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, 'btn-search')
    button.click()
    # browser.find_element_by_id("J_Itemlist_Pic_578812345477").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'icon').click()


login()
picking(1)
