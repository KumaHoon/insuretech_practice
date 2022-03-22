from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

driver = webdriver.Chrome('./chromedriver')


def rePlaceData(value) :
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i.decode('utf-8');
        result += decodedNumber
    return result
# 실습 2
# AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료를 가져와서 출력한다.

def getAIAData(name, birth, gender):
    driver.get(
        "https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#")
    driver.implicitly_wait(1)

    if name is not None:
        namebtn = driver.find_element_by_xpath('//*[@id="aia452730991"]')
        namebtn.send_keys(name)

    if birth is not None:
        birthInput = driver.find_element_by_xpath('//*[@id="aia644363719"]')
        birthInput.send_keys("19" + birth)
            
    # 남자를 클릭하라
    if gender == 0:
        # 남자 버튼를 클릭
        mbutton = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/label/div/div[1]')
        mbutton.click()
    elif gender == 1:
        # 여자 버튼을 클릭
        wbutton = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/label/div/div[2]')
        wbutton.click()
    
    resultBtn = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    resultBtn.click();
    driver.implicitly_wait(1)

    price = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]').text;
    print(price)

    driver.close()

def getLinaData(name, birth, gender):
    driver.get(
        "https://direct.lina.co.kr/product/ess/dtc01/easy")
    birthInput = driver.find_element_by_xpath('//*[@id="birthday"]')
    birthInput.send_keys(birth)
    # Case : 남자
    if gender == 0:
        mbutton = driver.find_element_by_xpath(
            '//*[@id="main_btn_male"]')
        mbutton.click()

    # Case : 여자
    elif gender == 1:
        wbutton = driver.find_element_by_xpath(
            '//*[@id="main_btn_female"]')
        wbutton.click()
    resultBtn = driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]/span')
    resultBtn.click();

    driver.implicitly_wait(2)
    price = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/div/table/tbody[1]/tr[1]/td[2]').text;
    print(price)


getLinaData("kumahoon", "001212", 1)