import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass

user_id = input('ID를 입력하세요: ')
user_pwd = getpass.getpass('PWD를 입력하세요(Not echoing): ')
print("(1/4) URL에 접속합니다...")
free_url = 'https://www.packtpub.com/packt/offers/free-learning'

# Chromedriver 실행 후 free_url 접속

driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver.exe')
driver.get(free_url)

# claim 버튼 클릭
print("(2/4) LOGIN을 실시합니다...")
btn_claim = driver.find_element_by_xpath("//input[@class='form-submit']")
ActionChains(driver).click(btn_claim).perform()

time.sleep(2)

# login form 버튼 클릭 및 id, pwd 입력 후 login 버튼 submit

btn_login_form = driver.find_element_by_xpath("//div[@class='respoLogin']")
ActionChains(driver).click(btn_login_form).perform()

input_id = driver.find_element_by_xpath("//input[@id='email']")
input_pwd = driver.find_element_by_xpath("//input[@id='password']")

input_id.send_keys(user_id)
input_pwd.send_keys(user_pwd)

btn_login = driver.find_element_by_xpath("//input[@id='edit-submit-1']")
ActionChains(driver).click(btn_login).perform()

if driver.find_element_by_xpath("//div[@id='messages-container']") is None:
    print("(3/4) LOGIN이 완료되었습니다...")
    
    time.sleep(4)

    # claim 버튼 클릭하여 free e-book 카트에 넣기
    
    btn_claim = driver.find_element_by_xpath("//input[@class='form-submit'][@value='Claim Your Free eBook']")
    ActionChains(driver).click(btn_claim).perform()
    print("(4/4) 공짜 책을 카트에 넣었습니다. 종료합니다.")

    today_book = driver.find_element_by_xpath("//div[@id='product-account-list']")
    today_book = today_book.text
    today_book = today_book.replace("\n","")
    today_book = today_book.split('+')
    print("\n오늘의 책은 다음과 같습니다:")
    print(today_book[0])
else:
    print("로그인이 잘못되었습니다. 이메일 주소와 비밀번호를 확인해주세요.")






# 종료

#driver.quit()
