from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r'D:\a.IT\Python\Automate\BrowserDrivers\chromedriver.exe'

def test_drive():
	browser = webdriver.Chrome(PATH)
	browser.get("https://www.google.com")
	print(browser.title)
	time.sleep(0.5)
	browser.quit()

def copy_link(playlist_url):
	browser = webdriver.Chrome(PATH)
	browser.get("https://www.google.com/search?q=tangthuvien&sxsrf=ALeKk03bK_ALKHWLpK9eLQ6tlrTZUWpYog%3A1618922646906&ei=lsx-YPHWNpn8wQPljof4CQ&oq=tangthuvien&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBQgAEMsBMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIFCAAQywEyBggAEAcQHlDIK1jIK2C0NWgAcAB4AIAB9QKIAb0FkgEDMy0ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwjx-aXq7IzwAhUZfnAKHWXHAZ8Q4dUDCA4&uact=5")

	search = browser.find_element_by_link_text("ngontinh")
	search.click()
	time.sleep(0.5)
	# browser.quit()

if __name__ == '__main__':
	playlist_url = "https://www.youtube.com/playlist?list=PLsNjtxNZOPpP65x2TeqP55d6CEP8TlFL-"
	copy_link(playlist_url)

