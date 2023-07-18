import mpmath

# Paste values between the third line
v = '''
199999999999999
19999999999999
1999999999999
199999999999
19999999999
1999999999
199999999
19999999
1999999
199999
19999
1999
199
19
1
'''  # and here

# outputs the above if the below is 0, 2, 15, False, 1: 30956745117962895292825159691675032847559175394706377094119397647307187439784996092023295962076506738837243562

number = 0  # addition, subtraction, multiplication and division will add to, subtract from, multiply by, and divide by each in array respectively
operation = 2  # operation: 0 = "add", 1 = "subtract", 2 = "multiply", 3 = "divide"
precision = 15  # dynamic precision (adjust as needed)
print_iterations = False  # option to print result after each iteration
output_option = 1  # output options: 0 = partial scientific, 1 = full, 2 = save to file, 3 = partial truncated

mpmath.mp.dps = 1000 + precision
values = v.strip().split('\n')
array = list(map(int, values))

if number == 0:
    total_result = mpmath.mpf(array.pop(0))
else:
    total_result = mpmath.mpf(number)

for i, value in enumerate(array):

    if operation == 0:
        total_result += value
    elif operation == 1:
        total_result -= value
    elif operation == 2:
        total_result *= value
    elif operation == 3:
        total_result /= value
    else:
        raise ValueError("Invalid operation. Please choose 0 for 'add', 1 for 'subtract', 2 for 'multiply', or 3 for 'divide'.")

    if print_iterations:
        print(f"Iteration {i+1}: {total_result}")

output_options = {
    0: f"The result in scientific notation is: {mpmath.nstr(total_result, 10, min_fixed=0, max_fixed=0)}",
    1: f"The full result is: {total_result}",
    2: "calcd.txt",
    3: f"The truncated result is: {str(total_result)[:101]}"
}

if output_option in output_options:
    if output_option == 2:
        with open(output_options[output_option], 'w') as f:
            f.write(str(total_result))
        print("The result has been saved to 'calcd.txt'.")
    else:
        print(output_options[output_option])
else:
    raise ValueError("Invalid output option. Please choose between 0, 1, 2, and 3.")
