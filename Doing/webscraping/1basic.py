from bs4 import BeautifulSoup

with open("Home.html", 'r') as home_html:
	content = home_html.read()
	# print(content)
# ------------------------------------------------------------ 
soup = BeautifulSoup(content, 'lxml')
# print all 
print(soup.prettify())
tags = soup.find_all('h5')
for tag in tags:
	print(tag)
# ------------------------------------------------------------- 
course_cards = soup.find_all('div', class_='card')
for card in course_cards:
	course_name = card.h5.text
	course_price = card.a.text.split()[-1]
	print(f"{course_name} cost: {course_price}")
# ------------------------------------------------------------ 


