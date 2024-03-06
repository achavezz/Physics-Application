# v_f = v_i + a * t
# missing_input: the variable missing to be calculated
# given_inputs: dictionary with key: given variable name, values: the variable's value
def first_kinematics_equation(missing_input, given_inputs):
    print("Using the first kinematics equation")
    
    # original equation
    if missing_input == 'final velocity':
        velocity_change = given_inputs['acceleration'] * given_inputs['time']
        usr_input = int(input("Enter the product of acceleration and time: "))
        while usr_input != velocity_change:
            usr_input = int(input("Try again: "))
        
        final_velocity = given_inputs['initial velocity'] + velocity_change
        res = float(input("Now add the initial velocity to the product: "))
        while res != final_velocity:
            res = float(input("Try again: "))    
        print("Correct!")

    # a = (v_f - v_i) / t
    if missing_input == 'acceleration':
        velocity_difference = given_inputs['final velocity'] - given_inputs['initial velocity']
        usr_input = int(input("Enter the velocity difference: "))
        while usr_input != velocity_difference:
            usr_input = int(input("Try again: "))
        
        acceleration = round(velocity_difference / given_inputs['time'], 2)
        res = float(input("Now divide the velocity difference by time: "))
        while res != acceleration:
            res = float(input("Try again: "))    
        print("Correct!")

    # t = (v_f - v_i) / a
    if missing_input == 'time':
        velocity_difference = given_inputs['final velocity'] - given_inputs['initial velocity']
        usr_input = int(input("Enter the velocity difference: "))
        while usr_input != velocity_difference:
            usr_input = int(input("Try again: "))
        
        time = round(velocity_difference / given_inputs['acceleration'], 2)
        res = float(input("Now divide the velocity difference by acceleration: "))
        while res != time:
            res = float(input("Try again: "))    
        print("Correct!")
    
    # v_i = v_f - a * t
    if missing_input == 'initial velocity':
        velocity_change = given_inputs['acceleration'] * given_inputs['time']
        usr_input = int(input("Enter the product of acceleration and time: "))
        while usr_input != velocity_change:
            usr_input = int(input("Try again: "))
        
        initial_velocity = given_inputs['final velocity'] - velocity_change
        res = float(input("Now subtract from the final velocity the product: "))
        while res != initial_velocity:
            res = float(input("Try again: "))    
        print("Correct!")

# v_f^2 = v_i^2 + 2*a*deltaX
def second_kinematics_equation(missing_input, given_inputs):
    print("Second")

# deltaX = v_i*t + 1/2 * a * t^2
def third_kinematics_equation(missing_input, given_inputs):
    print("Third")

# deltaX = 1/2(v_i + v_f)t
def fourth_kinematics_equation(missing_input, given_inputs):
    print("Fourth")

# param 1: missing variable to calculate
# param 2: map of given variables and their values
def determine_equation(missing_input, given_inputs):
    user_input_set = set([missing_input])
    for key in given_inputs:
        user_input_set.add(key)
    
    # call frozenset to create a set on a list of all possible variables for each KE equation
    # map, key: set of all possible variables, values: KE equation
    function_mapping = {
    frozenset(['final velocity', 'initial velocity', 'acceleration', 'time']): first_kinematics_equation,
    frozenset(['final velocity', 'initial velocity', 'acceleration', 'displacement']): second_kinematics_equation,
    frozenset(['displacement', 'initial velocity', 'acceleration', 'time']): third_kinematics_equation,
    frozenset(['displacement', 'initial velocity', 'final velocity', 'time']): fourth_kinematics_equation,
    }
    
    # from the set we created from user inputs, find an equivalent set to map to the correct KE Equation
    selected_function = None
    for inputs_set, func in function_mapping.items():
        if user_input_set == inputs_set:
            selected_function = func
            break

    if selected_function:
        selected_function(missing_input, given_inputs)
    else:
        print("No matching function found for the given inputs.")