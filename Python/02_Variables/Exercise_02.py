inp = input('>>> Enter Fahrenheit Temperature: ')

try:
	fahr = float(inp)
	cel = (fahr - 32) * 5.0 / 9.0
	print(round(cel, 4))
except:
	print('Please enter a number')