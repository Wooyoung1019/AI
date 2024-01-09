from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.set_window_size(1200, 800) # 设置浏览器窗口大小
browser.get('https://www.baidu.com/')
browser.implicitly_wait(10) # 设置隐式等待时间为10秒

kw_input = browser.find_element(By.ID, 'kw')
kw_input.send_keys('Python')
su_button = browser.find_element(By.CSS_SELECTOR, '#su')
su_button.click()

wait_obj = WebDriverWait(browser, 10) # 创建显示等待对象
wait_obj.until(
    expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, '#content_left')
    )
) # 设置等待条件（等搜索结果的div出现）
browser.get_screenshot_as_file('python_result.png') # 截屏
