#library
import time
import pytest
from optparse import Option
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest.mark.structures import Mark


option = webdriver.ChromeOptions()
# option.headless = True
option.add_experimental_option('excludeSwitches', ['enable-logging'])

#setup 
@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=option)
    driver.get('https://stgphr-hss.sibimapajak.id/')
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("bimaphr.user@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("jdGoRYk5vMMS0AXyV30CiDqjQvAvnmJz4Sh8xOZY")
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    yield driver
    # driver.quit()

#action
def test_beranda(driver):
    driver.find_element(By.XPATH, '//*[@id="dropdownProfile"]').click()
    driver.find_element(By.XPATH, '//*[@id="toLogout"]').click()
    assert 'Lupa Password' in driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div/div[4]/a').text

