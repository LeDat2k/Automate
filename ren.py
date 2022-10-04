#!/usr/bin/env python3
import os
import shutil
import unicodedata 	

def rename_unicode(source):
	os.chdir(source)

	for file in os.listdir(source):
		new_file = file
		if os.path.isdir(file):
			new_file = file.title()								# convert first character of each word to upper case
			new_file = new_file.replace(' ', '') 	# remove ' ' character
			shutil.move(file, new_file)
		else:
			new_file = file.replace(' ', '_')     # remove ' ' character
			new_file = unicodedata.normalize('NFKD', new_file).encode('ascii', 'ignore').decode() # change Unicode VN to EN
			shutil.move(file, new_file)

try:
	source = os.getcwd()
	rename_unicode(source)
except KeyboardInterrupt:
	print("Wrong!")