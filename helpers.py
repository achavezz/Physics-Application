# v_f = v_i + a*t
def first_kinematics_equation(missing_input, given_inputs):
    print(missing_input)
    print(given_inputs.keys())
    print(given_inputs.values())

# v_f^2 = v_i^2 + 2*a*deltaX
def second_kinematics_equation(missing_input, given_inputs):
    print("Second")

# deltaX = v_i*t + 1/2 * a * t^2
def third_kinematics_equation(missing_input, given_inputs):
    print("Third")

# deltaX = 1/2(v_i + v_f)t
def fourth_kinematics_equation(missing_input, given_inputs):
    print("Fourth")

# @param 1: missing variable to calculate
# @param 2: map of given variables and their values
def determine_equation(missing_input, given_inputs):
    user_input_set = set([missing_input])
    for key in given_inputs:
        user_input_set.add(key)
    
    function_mapping = {
    frozenset(['final velocity', 'initial velocity', 'acceleration', 'time']): first_kinematics_equation,
    frozenset(['final velocity', 'initial velocity', 'acceleration', 'displacement']): second_kinematics_equation,
    frozenset(['displacement', 'initial velocity', 'acceleration', 'time']): third_kinematics_equation,
    frozenset(['displacement', 'initial velocity', 'final velocity', 'time']): fourth_kinematics_equation,
    }
    
    selected_function = None
    for inputs_set, func in function_mapping.items():
        if user_input_set == inputs_set:
            selected_function = func
            break

    if selected_function:
        selected_function(missing_input, given_inputs)
    else:
        print("No matching function found for the given inputs.")