"""
PROBLEM 2 (50pts)

You are asked to write a program that allows the user to input a series of numbers.
Your program should store these numbers in a list. After the user has completed entering the numbers (but entering a 0),
your program should display the list, then determine and display the range of the numbers in the list.
The range is the difference between the highest and lowest value. Use f-strings to format the outputs when appropriate.

"""

def get_number_range():
    # creating an empty list
    user_input_list = []
    max_number = 0.0 # keep track of the highest number
    lowest_number =  0.0 # this will keep track of the lower number
    number_range = 0.0 # the different between high and low number
    # break when input is 0
    while True:
        user_num = float(input('Enter a number (0 to quit): '))
        if user_num == 0.0:
            break
        else:
            user_input_list.append(user_num)
    print(user_input_list)

    # if user only entered one 1 number then pressed 0 after
    if len(user_input_list) == 1:
        print('Only one number was entered so the number_range is 0')
    # after we gather the numbers. if statement to check if the list has more than 1 value
    if  len(user_input_list) > 1:
        max_number = max(user_input_list)
        lowest_number = min(user_input_list)

        #if low and high num is the same
        if max_number == lowest_number:
            print(f'The range value is {number_range} , because both the low and high numbers are equal')
        number_range = max_number - lowest_number
    else:
        print('You did not enter a number.')

    return number_range

the_range = get_number_range()
# display the range
print(f"The Range of the numbers in the list is {the_range}")



