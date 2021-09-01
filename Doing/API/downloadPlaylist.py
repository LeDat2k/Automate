from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
# take all URLs of youtube playlist -> store in a list

def webScraping():
    # url = str(input('Playlist URL: '))
    url = "https://www.youtube.com/playlist?list=PLsNjtxNZOPpP65x2TeqP55d6CEP8TlFL-"
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')

    # print(soup.prettify())
    tags = soup.find_all('div', id='container')
    tags2 = soup.find_all(class_="style-scope ytd-playlist-video-list-renderer")
    tags3 = soup.select('body') 
    print(tags3)
    # print(len(tags)
    for tag in tags3:
        print(tag.text) 

    # return link_list


# write it in .txt file, 1 line 1 url
def savelink():
    link_list = webScraping()
    with('playlistLink.txt', 'a') as file:
        file.open()
        for link in len(link_list):
            file.write(link)
        file.close() 

# first link open aliexpress page

def openPlaylist():
    browser = webdriver.Firefox()
    url = "https://www.youtube.com/playlist?list=PLsNjtxNZOPpP65x2TeqP55d6CEP8TlFL-"
    browser.get(url)

    # link1 = browser.find_element_by_name('ytd-playlist-video-renderer')
    # link2 = browser.find_element_by_tag_name('ytd-playlist-video-renderer')
    link3 = browser.find_element_by_class_name('style-scope ytd-playlist-video-list-renderer')
    # print(link1)
    # print(link2)
    print(link3)

    browser.quit()



if __name__=="__main__":
    # webScraping()
    openPlaylist()
    # GUI or youtube API


