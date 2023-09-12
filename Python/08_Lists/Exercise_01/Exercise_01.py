xFile = "romeo.txt"

with open(xFile, 'r') as arquivo:

	palavras = []

	for line in arquivo:
		words = line.split()

		palavras.extend(words)

	palavras.sort()
	print(palavras)