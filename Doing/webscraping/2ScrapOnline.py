from bs4 import BeautifulSoup
import requests

def remove_tab(Cstring):
	c_name = ""
	for ch in Cstring:
		if ch == '	': # ch == 'tab'
			break
		c_name = c_name + ch

	return c_name

# I try a lot to fix the string in Skill make it can tab but i can't, 09:34 PM 03/07/21

def webScrapping(html_text):
	soup = BeautifulSoup(html_text, 'lxml')
	jobs = soup.find_all('li', class_='clearfix joblistli')
	for job in jobs:
		company_name = job.find('h3', class_='joblist-comp-name').text
		skills = job.find('span', class_='srp-skills').text

		link = job.header.h2.a['href']

		# print(type(company_name)) # string
		company_name = remove_tab(company_name.strip())
		print("---Company's name: {}\n".format(company_name.strip()))

		print("---Require skills:")
		print(f'{skills.strip()}')
		print('--------------------------')

		print(f"Links: {link}")

		print('------------------------------------------------------------')

def main():
	html_text = requests.get('https://www.timesjobs.com/jobskill/python-jobs').text
	webScrapping(html_text)
	print("\n!!!Done!!!")

main()