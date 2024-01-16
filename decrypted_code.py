global_variable = 100
my_dict = {'key1': 'value1', 'ke12': 'value2', 'ke13': 'value3'}


def process_numbers():
    global global_variable  # Declare global_variable as global
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers


my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # Removed unnecessary argument (numbers=m1_set)


def modify_dict(local_variable):  # Added missing argument
    my_dict['ke14'] = local_variable


modify_dict(10)  # Passed 10 as an argument


def update_global():
    global global_variable
    global_variable += 10


for i in range(5):
    print(i)
    # I += 1  # Commented out this line as it's unnecessary within the loop

# Checked if my_set is not None and my_dict['ke14'] == 10
if my_set is not None and my_dict.get('ke14') == 10:
    print("Condition met!")

# Checked if 5 not in my_dict
if 5 not in my_dict.values():  # Corrected the condition to check values
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
