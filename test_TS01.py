#library
from ssl import Options
import time
import pytest
from optparse import Option
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest.mark.structures import Mark

#key negatif test
userAkses = [
    ("",""),
    ("","jdGoRYk5vMMS0AXyV30CiDqjQvAvnmJz4Sh8xOZY"),
    ("bimaphr.user@gmail.com",""),
    ("bimaphr.userrrr@gmail.com","jdGoRYk5vMMS0AXyV30CiDqjQvAvnmJz4Sh8xOZY"),
    ("bimaphr.user@gmail.com","123456789")
]

option = webdriver.ChromeOptions()
option.headless = True
option.add_experimental_option('excludeSwitches', ['enable-logging'])

#setup 
@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=option)
    driver.get('https://stgphr-hss.sibimapajak.id/')
    driver.implicitly_wait(30)
    driver.get_screenshot_as_file("testing1.png")
    yield driver
    driver.quit()

#action
def test_login_succes(driver):
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("bimaphr.user@gmail.co")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("jdGoRYk5vMMS0AXyV30CiDqjQvAvnmJz4Sh8xOZY")
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    assert 'Beranda' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text
    driver.get_screenshot_as_file("testing1.png")

@pytest.mark.parametrize('email, password', userAkses)
def test_login_fail(driver, email, password):
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    assert 'Surel' in driver.find_element(By.XPATH, '//*[@id="emailInput"]/label').text
    



