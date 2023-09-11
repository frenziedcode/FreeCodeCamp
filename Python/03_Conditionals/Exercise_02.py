xh = input('Enter Hours: ')
xr = input('Enter Rate: ')

dif_xh = 0

try:
	xh = int(xh)
	xr = int(xr)
	if (xh >= 40):

		xp = 40 * xr

		dif = xh - 40
		xr = xr * 1.5 * dif
		print(xr + xp)

	elif (xh < 40):
		xp = xh * xr
		print(xp)

except:
	print('Error, please enter numeric input')
