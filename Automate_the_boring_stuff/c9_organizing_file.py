import shutil, os
# ------------------------------------------------------------ 
# copy & move file
os.chdir('C:\\Users\\ASUS\\Downloads')
shutil.copy('test1.txt', 'D:\\1.IT\\Python\\Automate\\zFolder')
shutil.copy('test1.txt', 'D:\\1.IT\\Python\\Automate\\zFolder\\test3.txt')

# shutil.copytree('C:\\Users\\ASUS\\Downloads\\fold', 'D:\\1.IT\\Python\\Automate\\zfolder')

# shutil.move('C:\\Users\\ASUS\\Downloads\\test2.txt', 'D:\\1.IT\\Python\\Automate\\zFolder')


# ------------------------------------------------------------
# permanently delete file/folder

# os.unlink(path) # del file
# shutil.rmtree(path) # del folder

# for fileName in os.listdir(path):
# 	if fileName.endwith('.rxt'):
# 		os.unlink(fileName)

# ------------------------------------------------------------ 
# safe delete with the send2trash module
# ??????????????

# ------------------------------------------------------------
# zip file
# ??????????????????????????????

# ------------------------------------------------------------
# Project: move file in Download folder


# Project: Rename file 

