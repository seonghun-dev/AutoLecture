from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#크롬 Open
browser = webdriver.Chrome('D:/chromedriver.exe')
browser.get('https://ecampus.konkuk.ac.kr/ilos/main/member/login_form.acl')

#로그인
elem = browser.find_element_by_id("usr_id")
elem.send_keys("seonghun912")

elem = browser.find_element_by_id("usr_pwd")
password = input("비밀번호를 입력하세요.")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)


#필요한 강의 접근
search = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[2]/ol/li[20]/em")
search.click()

#필요한 강의 접근
n = 1 #강의 주차
xpath = "/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/div[" + str(n) + "]"
el = browser.find_element_by_xpath(xpath)
el.click()

start = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/div/ul/li[2]/img")
start.click()

sleep(15)
startvid = browser.find_element_by_xpath("/html/body")
startvid.click()

sleep(900)
n = n + 1
browser.get("http://ecampus.konkuk.ac.kr/ilos/st/course/online_list_form.acl?WEEK_NO=" + str(n))

while True:
    start = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/div/ul/li[2]/img")
    start.click()

    sleep(2)
    startvid = browser.find_element_by_xpath("/html/body")
    startvid.click()
    #startvid.click()

    sleep(900)


    n = n + 1
    browser.get("http://ecampus.konkuk.ac.kr/ilos/st/course/online_list_form.acl?WEEK_NO=" + str(n))
    '''
    # 종료
    xpath = "/html/body/div[2]/div[2]/div[1]/div[2]"
    end = browser.find_element_by_xpath(xpath)
    end.click()
    '''
    # 알림처리
    '''
    alert = browser.switch_to.alert
    if alert == 1:
        alert.accept()
        sleep(2)
    '''

'''
while True:  # 무한반복
    xpath = "/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div[2]"
    el = browser.find_element_by_xpath(xpath)
    if el.text == '1/1':
        el.click()
        break

search = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/div/ul/li[2]/img")
search.click()

sleep(25)

# 종료
xpath = "/html/body/div[2]/div[2]/div[1]/div[2]"
end = browser.find_element_by_xpath(xpath)
end.click()

start = browser.find_element_by_xpath("/html/body/div[2]/div/button")
start.click()

xpath = "/html/body/div[2]/div/div[4]/div[4]/span[2]"
full = browser.find_element_by_xpath(xpath)

'''
