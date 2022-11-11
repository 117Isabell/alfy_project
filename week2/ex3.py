def input_list():
    """ the user_list() function
    collects numbers from user input,
    calculate their sum and return it as a list
		(We recommend creating a helper function named
		input_list_helper for collecting the user input
    :return: list of numbers that were given
    by the user, the last object is the sum of all the others
    """

    ## 1. capture
    ## 2. keep number in a list
    ## 3. if input is empty => we output the list and get the sum

    input_numbers = []

    while True:
        val = input("Enter your number: ")
        if val == '':
            ## cal sum
            sum = my_sum(input_numbers)
            input_numbers.append(sum)
            ## print the list
            print(input_numbers)
            break
        val = float(val)
        input_numbers.append(val)

def my_sum(my_list):
    sum = 0
    for number in my_list:
        sum += number
    return sum

input_list()

