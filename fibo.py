# lets create a input variable that ask for the sequence

nth_term = int(input('please enter the number of sequences you want to see: '))

# count variable that  will be used to break the while loop
count = 0
# everytime the loop starts over it will update count
# it will have 2 numbers
number1, number2 = 0, 1

if nth_term <= 0:
    print('Please enter a positive integer!')
elif nth_term == 1:
    print('this is your sequence',nth_term,':')
    print(number1)
else:
    print('The Fibbonaci sequence:')
    while count < nth_term:
        print(number1)
        nth = number1 + number2
        number1 = number2
        number2 = nth
        count = count + 1
    

