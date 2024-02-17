# prompts the user for their name
user_name = input('What is your name? ')

def hello_name(user_name):
    return print('Hello ' + user_name + '!\n')

hello_name(user_name)


def first_odds():
    # for loop that goes through a range containing 100 numbers
    for num in range(100):
        # if num divided by 2 has a remainder it is an odd number
        if(num % 2 != 0):
            print(str(num) + ' is even.')
    return

first_odds()

list1 = [2,8,6,4,10]

def max_num_in_list(a_list):
    print('\n' + 'The current list contains: ' + str(a_list))
    max_num = 0
    # goes through list and checks if the current number is greater than the current max_number
    for num in a_list:
        # assign current number to max_num variable if its greater than the previous value
        if (num > max_num):
            print(str(num) + ' is greater than ' + str(max_num) + '.')
            max_num = num
    return print(str(max_num) + ' is the max number.' + '\n')

max_num_in_list(list1)

# prompts the user for an input to be checked
user_year = int(input('Please input a year to check for leap year qualifications: '))

def is_leap_year(a_year):
    # if the year modulus 4 results in 0 move to next condition
    if (a_year % 4 == 0):
        # if the year resolves with a remainder it is a leap year
        if(a_year % 100 > 0):
            year = True
            return print('Is ' + str(a_year) + ' a leap year?: ' + str(year) + '\n')
        # if the year modulus resolves with no remainer it can't be a leap year.
        else:
            year = False
            return print('Is ' + str(a_year) + ' a leap year?: ' + str(year) + '\n')
    # if the modulus 4 resolves with a remainder it can't be a leap year
    else:
        year = False
        return print('Is ' + str(a_year) + ' a leap year?: ' + str(year) + '\n')
    
is_leap_year(user_year)

con_list = [2,3,4,5,6,7]

non_con_list = [1,2,4,5]

def is_consecutive(a_list):
    print('This will check if the given list containing ' + str(a_list) + ' is consecutive.')           
    consecutive = True 
    # last num = the value at index 0
    last_num = a_list[0]
    # for every number in a list starting at index 1
    for num in a_list[1:]:
        # if the current number = last_num + 1
        if (num == last_num+1):
            print('Is ' + str(num) + ' greater than ' + str(last_num) + ' by exactly 1?: ' + str(consecutive))
            # Assign last number to the current number of the loop
            last_num = num
        else:
            consecutive = False
            print('Is ' + str(num) + ' greater than ' + str(last_num) + ' by exactly 1?: ' + str(consecutive))
            return print('Is the list consecutive?: ' + str(consecutive) + '\n')
    return print('Is the list consecutive?: ' + str(consecutive) + '\n')
    
# function for the consecutive list
is_consecutive(con_list)

# function for the non consecutive list
is_consecutive(non_con_list)
