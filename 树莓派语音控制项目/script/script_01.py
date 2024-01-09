import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Chrome() # 创建Chrome浏览器对象
browser.get('https://www.baidu.com/') # 加载指定页面

kw_input = browser.find_element(By.ID, 'kw') # 通过元素id获取元素
kw_input.send_keys('Python') # 模拟用户输入行为
su_button = browser.find_element(By.CSS_SELECTOR, '#su') # 通过css选择器获取元素
su_button.click() # 模拟用户点击行为

time.sleep(5)

next_page = browser.find_element(By.CSS_SELECTOR, "a[class='n']")

actions = ActionChains(browser)
actions.move_to_element(next_page).click(next_page).perform()
actions.perform()
time.sleep(5)

