fileName = input("Enter a file name: ")
openFile = open(fileName)

for line in openFile:
	if line.startswith('X-DSPAM-Confidence:') :
		print(line)