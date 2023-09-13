import re

def arithmetic_arranger(a) :

	linha1 = ""
	linha2 = ""
	linha2a = ""
	linha3 = ""
	linha4 = ""

	for calc in a :
		str_calc = str(calc)
		tempNum = re.findall(r'\d+', calc)
		symbol = re.findall(r'[-+*/]', calc)

		intNum0 = int(tempNum[0])
		intNum1 = int(tempNum[1])

		if symbol == ['+']:
			symbol = "+"
			result = intNum0 + intNum1
		elif symbol == ['-']:
			symbol = "-"
			result = intNum0 - intNum1
		else:
			print("Error: Operator must be '+' or '-'")
			exit()

		linha1 += f" {intNum0 : >5} "
		linha2 += f" {symbol : <4}"
		linha2a += f" {intNum1 : >3}"
		linha3 += "----     "
		linha4 += f" {result  : >2}   "

	print(len(tempNum[0]))
'''
	print(linha1.rstrip())
	print(linha2.rstrip())
	print(linha3)
	print(linha4.rstrip())
'''
	#	print(f"{intNum0 : > 5}")

	#	intNum1 = int(tempNum[1])
	#	print(symbol,  intNum1)
'''
		if symbol == "+"   :
			result = intNum0 + intNum1
			print("-----")
			print(result)
		elif symbol == "-" :
			result = intNum0 - intNum1
			print(result)
		elif symbol == "*" :
			result = intNum0 * intNum1
			print(result)
		elif symbol == "/" :
			result = intNum0 / intNum1
			print(result)
'''
#Call Function
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])



'''
num1 = 235
num2 = 52
sumTotal = num1 + num2

str_num1 = str(num1)
str_num2 = str(num2)
str_sumTotal = str(sumTotal)

maxWeight = max(len(str_num1), len(str_num2), len(str_sumTotal))

print(f"{str_num1  : >5}")
print(f"{str_num2 : >5}")
print("-----")
print(f"{sumTotal : >5}")
'''