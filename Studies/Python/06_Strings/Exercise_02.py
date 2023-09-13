print("PALINDROME")

word1 = "Hello, World!"
wordInv = ""

wordCompare = "abc"


word1 = input("Write one word: ")
for i in word1:
	wordInv = i + wordInv
	wordInv = wordInv.lower()

if (wordInv == word1):
	print(word1.capitalize(), "is palindrome")
else:
	print(word1.capitalize(), "not is palindrome")

