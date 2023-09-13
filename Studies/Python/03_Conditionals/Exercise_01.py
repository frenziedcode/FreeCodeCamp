xh = input('Enter Hours: ')
xh = int(xh)
xr = input('Enter Rate: ')
xr = int(xr)

dif_xh = 0

if (xh >= 40):

	xp = 40 * xr

	dif = xh - 40
	xr = xr * 1.5 * dif
	print(xr + xp)

elif (xh < 40):
	xp = xh * xr
	print(xp)

