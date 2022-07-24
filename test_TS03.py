#library
from ssl import Options
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
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("bimaphr.user@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("jdGoRYk5vMMS0AXyV30CiDqjQvAvnmJz4Sh8xOZY")
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    yield driver
    # driver.quit()

#action
def test_beranda(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[1]/a').click()
    assert 'Beranda' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_notifikasi(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[2]/a').click()
    assert 'Notifikasi' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_detail_transaksi(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[4]/a').click() 
    assert 'Transaksi' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text    

def test_rekapitulasi(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[5]/a').click()
    assert 'Rekapitulasi' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_besaran_pajak(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[7]/a').click()
    assert 'Besaran Pajak' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_wajip_pajak(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[8]/a').click()
    assert 'Wajib Pajak' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_tempat_usaha(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[9]/a').click()
    assert 'Tempat Usaha' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_pemetaan(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[10]/a').click()
    assert 'Pemetaan' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_pengguna(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[12]/a').click()
    assert 'Pengguna' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text    

def test_starter_key(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[13]/a').click()
    assert 'Starter Key' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_generate_starter_key(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[14]/a').click()
    assert 'Generate Starter Key' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_hak_akses(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[15]/a').click()
    assert 'Hak Akses' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text

def test_aktifitas_log(driver):
    driver.find_element(By.XPATH, '//*[@id="sidenav"]/ul/li[16]/a').click()
    assert 'Aktifitas Log' in driver.find_element(By.XPATH, '//*[@id="titlePage"]').text