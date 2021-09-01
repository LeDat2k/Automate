import time, datetime
from selenium import webdriver

# file_tail = ['.py', '.pyw', '.ps1', '.bat']
# fileName_list = ['a.txt', 'b.bat', 'c.py', 'd.txt']

# now = datetime.datetime.now()

# s = "Lê Phước Đạt".lower()

# print(s.find("Lê")) # 0
# print(s.find("Le".lower()))
# print(s.find("le"))
# print(s.find("LE"))
# print(s.find("lÊ".lower()))
# print(s.find("LÊ".lower()))


# PATH = r"C:\Users\ASUS\Downloads\edgedriver_win64\msedgedriver.exe"
# browser = webdriver.Edge(PATH)
# browser.get('https://truyen.tangthuvien.vn/')
# time.sleep(3)
# browser.close()


# now = datetime.datetime.now()
# time = datetime.datetime(now.year, now.month, now.day, 14, 0,0)
# t = time-now
# print (t.total_seconds())

# t1 = datetime.datetime(2000,1,1,19,89,0)
# t2 = datetime.datetime(2000,1,2,7,0,0)
# print((t2-t1))

def rename_white_name(s):
	s.strip()
	s.lstrip()
	s.rstrip()
	return s.replace(' ', '_')

if __name__ == '__main__':
	s = "Document 1.docx"
	print(rename_white_name(s))
	print(s.strip())
	# print(s.replace(' ', '_'))
