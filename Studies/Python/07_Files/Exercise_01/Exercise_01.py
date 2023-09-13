xFile = open('mBook.txt')
countLines = 0

for i in xFile:
	countLines = countLines + 1
print(i, "\nLines: ",countLines)