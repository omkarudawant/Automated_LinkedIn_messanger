from selenium import webdriver
import sys

username = sys.argv[1]
password = sys.argv[2]

browser = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

def extract():
	browser.find_elements_by_xpath("//*[@id='username']")[0].send_keys(username)  # login_email
	browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(password)  # login_password
	browser.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0].click()  # login_btn 
	browser.find_elements_by_xpath('//*[@id="messaging-nav-item"]')[0].click()  # msgs_btn

if __name__ == "__main__":
    extract()

