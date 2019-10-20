print("give me two numbers and I'll divide them.")
print("enter 'q' to quit.")

while True:
	first_number = input('\nFirst number: ')
	if first_number == 'q':
		break
	second_number = input('Second number: ')
	try:
		answer = int(first_number)/ int(second_number)
	except ZeroDivisionError:
		print('you cannot divide by 0! ')
	else:
		print(answer)
