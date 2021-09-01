from bs4 import BeautifulSoup
import requests

def webScrapping(html_text, unfamiliar_skill):
	soup = BeautifulSoup(html_text, 'lxml')
	jobs = soup.find_all('li', class_='clearfix joblistli')
	for job in jobs:
		company_name = job.find('h3', class_='joblist-comp-name').text
		skills = job.find('span', class_='srp-skills').text
		detail = job.find('ul', class_="job-more-dtl clearfix").text
		link = job.header.h2.a['href']

		if unfamiliar_skill not in job:
			# print(type(company_name)) # string
			with open()
			print("Company's name is {}".format(company_name.strip()))
			print(f"skills: {skills.strip()}")
			print(f"Detail: {detail.strip()}")
			print(f"Links: {link}")

		# print(detail)	


def main():
	print("what you don't have? ")
	unfamiliar_skill = input('>>')
	print("Filter out...")

	html_text = requests.get('https://www.timesjobs.com/jobskill/python-jobs').text

	webScrapping(html_text, unfamiliar_skill)

	print("DONE!!")

main()