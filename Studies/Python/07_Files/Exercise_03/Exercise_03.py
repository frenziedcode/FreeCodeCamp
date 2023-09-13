xFile = open('mBook.txt')

for line in xFile:
	line = line.rstrip()
	if line.startswith('Sed') :
		print(line)