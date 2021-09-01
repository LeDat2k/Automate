import shutil, os, sys

def rename_file(path):
	os.chdir(path)

	for name in os.listdir():
		new_name = name.replace(' ', '_')	
		shutil.move(name, new_name)


if __name__ == '__main__':
	# get now path folder path

	folder = os.getcwd()
	folder2 = sys.argv[0]

	# print(folder2)
	# print(folder)
	# rename_file(os.path.dirname(folder2))
	rename_file(folder)
	