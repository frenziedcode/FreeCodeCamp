fileName = input("Enter a file name: ")
openFile = open(fileName)

for line in openFile:
	print(line.upper())