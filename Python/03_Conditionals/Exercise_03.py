score = input('Enter the score number: ')
score = float(score)

if ( score > 0.0 and score <= 1.0):

	if (score >= 0.9):
		print('Grade A')
	elif(score >= 0.8):
		print('Grade B')
	elif(score >= 0.7):
		print('Grade C')
	elif(score >= 0.6):
		print('Grade D')
	elif(score < 0.6):
		print('Grade F')
else:
	print('The score is out of range!')