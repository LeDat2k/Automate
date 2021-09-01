import os, shutil, time
import itertools, threading, sys # for loading animate

# done = False
#here is the animation for loading
def animate():
	# itertools.cycle -> infinity loop cycle 
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rRunning ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
      
    sys.stdout.write('\r!!! Done !!!     ')

def move_exeFile(source, exe_destination):
	os.chdir(source)

	file_tail = ('.exe', '.msi')

	for fileName in os.listdir(source):
		if fileName.endswith(file_tail):
			shutil.move(fileName, exe_destination)

def rename_mp3(source):
	os.chdir(source)

	remove_text = ['y2mate.com - ', 'Lyric', 'lyric', 'Vietsub', 'Tik Tok']

	for fileName in os.listdir(source):
		if fileName.endswith('.mp3'):
			newFileName = fileName
			for text in remove_text:
				newFileName = newFileName.replace(text, '')

			shutil.move(fileName, newFileName)	
		
def move_mp3_file(source, mp3_destination):
	os.chdir(source)

	for fileName in os.listdir(source):
		if fileName.endswith('.mp3'): 
			shutil.move(fileName, mp3_destination)

def main():
	source = r'C:\Users\ASUS\Downloads'
	exe_destination = r'D:\Installer'
	mp3_destination = r'D:\Music' 
	if not os.path.exists(exe_destination) or not os.path.exists(mp3_destination):
		print("Error PATH NOT FOUND!")
		time.sleep(1)
		return

	move_exeFile(source, exe_destination)

	rename_mp3(source)
	move_mp3_file(source, mp3_destination)

try:
	print("\tAuto move file in Downloads folder")

	# still run function() when time.sleep() active
	# t = threading.Thread(target=animate)
	# t.start()

	sys.stdout.write('Running ... ')
	main()
	sys.stdout.write('\r!!!!Done!!!!')	
		
except KeyboardInterrupt: # Ctrl + C
	#long process here
	# done = True
	# time.sleep(0.5)
	sys.stdout.write('\r!!! Done !!!   ')