# soo lets ask for the number of sequence they want:
# lets take its integer value cos an input function always return a string

sequence = int(input('How many terms do you want?'))

# there will be 2 numbers
number1 = 0
number2 = 1

# a count variable:
count = 0


if sequence <= 0:
	print('Please enter a positive integer!')

elif sequence == 1:
	print('the sequence is',sequence,':')

else:
	while count <= sequence:
		print(number1)
		print('Here is the Fibbonaci Sequence:')
		number1 = number2
		number2 = sequence
		count =+ count

