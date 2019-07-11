from selenium import webdriver
import sys

username = sys.argv[1]
password = sys.argv[2]

browser = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

def extract():
	login_id = browser.find_elements_by_xpath("//*[@id='username']")[0]
	login_id.send_keys(username)
	login_pass = browser.find_elements_by_xpath("//*[@id='password']")[0]
	login_pass.send_keys(password)
	login_btn =browser.find_elements_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')[0]
	login_btn.click()
	msgs_btn = browser.find_elements_by_xpath('//*[@id="messaging-nav-item"]')[0]
	msgs_btn.click()


if __name__ == "__main__":
    extract()

