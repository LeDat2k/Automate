import csv

e_File = open('example.csv')
e_reader = csv.reader(e_File)
e_data = list(e_reader)

# print(e_data)

e_data[row][column]
# ------------------------------------------------------------
# read file with for loop

for row in e_reader:
print('Row #' + str(e_reader.line_num) + ' ' + str(row))

# ------------------------------------------------------------
# write object




