import os, winshell, win32com.client, shutil

def create_shortcut(source, file_tail):
	os.chdir(source)

	# file to create shortcut
	# file_tail = ('.py', '.pyw', '.ps1', '.bat')

	# delete shortcut if exist
	remove_file(source, '.lnk')

	for file_name in os.listdir():
		if file_name.endswith(file_tail):
			path = os.path.join(source, file_name + '.lnk')
			target = os.path.join(source, file_name)
			icon = target

			shell = win32com.client.Dispatch('WScript.Shell')
			shortcut = shell.CreateShortCut(path)
			shortcut.Targetpath = target
			shortcut.IconLocation = icon
			shortcut.save()

def remove_file(source, file_tail):
	os.chdir(source)

	# delete shortcut if exist
	for file_name in os.listdir():
		if file_name.endswith(file_tail):
			path = os.path.join(source, file_name)
			os.unlink(path)

def move_file(source, destination, file_tail):
	remove_file(destination, file_tail)

	os.chdir(source)

	for file_name in os.listdir():
		if file_name.endswith(file_tail):
			shutil.move(file_name, destination)

def copy_file(source, destination, file_tail):
	remove_file(destination, file_tail)

	os.chdir(source)

	for file_name in os.listdir():
		if file_name.endswith(file_tail):
			shutil.copy(file_name, destination)

def main():
	# source = r"D:\Code\Python\Automate\Done"
	# source = os.getcwd()	
	source = os.path.abspath('./')
	
	# source = os.path.abspath('.') don't use this cuz os.path.abspath('.') will the path of the shortcut in start folder
	# (where the file execute), therefore can't create any shortcut
	# -> run wrong when use shortcut but run good when use the own file not shortcut
	
	# shortcut_path= 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Automate'
	# startup_path_auto = r"D:\Code\Python\Automate\Done\Startup"
	startup_path_auto = os.path.abspath("./Startup/")
	startup_path_win = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	
	# create shortcut for file end with .py .pyw .ps1 .bat 
	# create_shortcut(source, ('.py', '.pyw', '.ps1', '.bat'))
	# # move file to Automate folder in start menu
	# move_file(source, shortcut_path, '.lnk')

	# # create shortcut again for startup folder
	create_shortcut(startup_path_auto, ('.py', '.pyw', '.ps1', '.bat'))
	# # move file to start up folder
	move_file(startup_path_auto, startup_path_win, ('.pyw.lnk', '.py.lnk', '.bat.lnk'))

try:
	main()
	print('Successfull')
except KeyboardInterrupt:
	print('Error')