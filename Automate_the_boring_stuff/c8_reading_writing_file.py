import os
path = os.path.join('usr', 'bin', 'spam')
print(path)

os.listdir(path) # -> return a list of all files/folders in dir path
# ---------------------------------------------------------
myFiles = ['a.txt', 'b.docx', 'c.csv']
for fileName in myFiles:
    print(os.path.join('C:\\Users\\ASUS\\Documents', fileName))
# j---------------------------------------------------------

# get current directory path
curDir = os.getcwd()
print(curDir)

# os.chdir('C:\\')


# j------------------------------------------------------------
# create new folder
# os.makedirs('D:\\1.IT\\Python\\Automate\\netruyen\\truyentranh')

# ------------------------------------------------------------ 
# absolute vs relative path
abs_path = os.path.abspath('.')
print(abs_path)

# os.path.relpath('')
# [????????????]

path = os.getcwd() # D:\\1.IT\\Python\\Automate
a = os.path.basename(path)  
print(a)
b = os.path.dirname(path)
print(b)

print(os.path.sep) # \ in win 10 but / in linux and Mac OS
# ------------------------------------------------------------
# file size vs folder contents

x = os.path.getsize('D:\\1.IT\\Python\\Automate\\c8_reading_writing_file.py')
print(x) # -> in byte

# ------------------------------------------------------------
#checkinng path validity

# >>> os.path.exists('C:\\Windows')
# True
# >>> os.path.exists('C:\\some_made_up_folder')
# False
# >>> os.path.isdir('C:\\Windows\\System32')
# True
# >>> os.path.isfile('C:\\Windows\\System32')
# False
# >>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
# False
# >>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
# True

# ------------------------------------------------------------
# 3 step to deal with a file
# - open()
# - read() or write()
# - close()

file = open('D:\\1.IT\\Python\\Automate\\znote.txt')

# file = open('D:\\1.IT\\Python\\Automate\\znote.txt', 'r')
file_content = file.read()
file.readlines()
file.close()

file = open('D:\\1.IT\\Python\\Automate\\znote.txt', 'w')
file.write('>>>>>This line python program writes')
file.close()
# can read and write file
# file = open('D:\\1.IT\\Python\\Automate\\znote.txt', 'a')

# ------------------------------------------------------------
# save variables with the shelve ||pprint.pformat()
# ????????
# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# cats
# pprint.pformat(cats)
# ???????
# ------------------------------------------------------------


