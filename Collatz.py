#Author: Darragh Murphy

#take in input
#split two numbers into 2 variables
#lOOP_1
#loop through values between 2 variables
#LOOP_2
#check if even
#then divide by 2
#check if odd
#then multiply by 3 and 1
#if 1 then break loop
#LOOP_2
#LOOP_1

user_input = input('Enter two digits seperated by a space: ')
print(user_input)
user_input = user_input.split(' ')
i = int(user_input[0])
j = int(user_input[1])

while i != 1:
    if i % 2 == 0:
        i = i // 2
        print(i)
    else:
        i = i * 3 + 1
        print(i)
