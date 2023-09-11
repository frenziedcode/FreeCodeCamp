num1 = "abc"
num2 = []
result = 0
i = 0
maxNum = 0
minNum = 0

#Enter a number when is != "done"
while(num1 != "done"):
	num1 = input(">>> Enter a number: ")

	if (num1 != "done"):
		try:
			num2.append(int(num1))
		except:
			print("Invalid input")

# Maximum Number
for i in num2:
	result = result + i
	if ( i > maxNum):
		maxNum = i
	minNum = maxNum
	if (i < minNum):
		minNum = i


print("Maximum Number: ", maxNum, "\nMinimum Number: ", minNum, "\nResult: ", result)