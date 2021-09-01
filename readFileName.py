import sys, os

file_path = os.getcwd()

file_name1 = sys.argv[0] # get name of file after command, ex: updrive test.txt test2.txt (file_name = test.txt vs test2.txt)

for arg in sys.argv:
    print(arg)

# file_name1 = file_name1[2:]    
# file_name2 = sys.argv[1]
# file_name2 = file_name2.split(os.path.sep())

print("{}     {}".format(file_path, file_name1))
# print(file_name2)

print()