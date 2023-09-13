num1 = "abc"
num2 = []
result = 0
count = 0

i = 0
while(num1 != "done"):
	num1 = input("Enter a number: ")

	if num1 != "done":
		try:
			num2.append(int(num1))
			count = count + 1
		except:
			print("Invalid input")

for i in num2:
	result = result + i

print(result, count, result / count)
