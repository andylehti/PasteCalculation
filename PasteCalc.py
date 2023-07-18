import mpmath
import re
import math

def calculate_result(v, number, operation, precision, output_option):
    mpmath.mp.dps = 1000 + precision

    lines = v.split('\n')

    array = []
    for line in lines:
        values = re.findall(r'\d+', line)
        if values:
            array.extend(map(int, values))

    if number == 0:
        total_result = mpmath.mpf(array.pop(0))
    else:
        total_result = mpmath.mpf(number)

    result_strings = []  # To store the equations of each iteration

    for i, value in enumerate(array):
        last_result = total_result

        if operation == 0:
            total_result += value
            operation_symbol = '+'
        elif operation == 1:
            total_result -= value
            operation_symbol = '-'
        elif operation == 2:
            total_result *= value
            operation_symbol = '⋅'
        elif operation == 3:
            total_result /= value
            operation_symbol = '/'
        else:
            raise ValueError("Invalid operation. Please choose 0 for 'add', 1 for 'subtract', 2 for 'multiply', or 3 for 'divide'.")

        if output_option[0] == -1:
            output_result = f"{mpmath.floor(total_result)}"
        elif output_option[0] == 0:
            output_result = f"{mpmath.nstr(total_result, 10, min_fixed=0, max_fixed=0)}"
        elif output_option[0] == 1:
            output_result = f"{math.ceil(total_result)}"
        elif output_option[0] == 2:
            output_result = f"{total_result}"
        elif output_option[0] == 3:
            output_result = f"{str(total_result)[:101]}"

        if output_option[3]:  # show_equation is True
            result_string = f"{last_result} {operation_symbol} {value} = {output_result}"
        else:
            result_string = f"{output_result}"

        result_strings.append(result_string)

        if output_option[2]:  # print_iterations is True
            print(result_string)

    # Final output result
    if output_option[0] == -1:
        final_output = f"The full rounded down result is: {mpmath.floor(total_result)}"
    elif output_option[0] == 0:
        final_output = f"The result in scientific notation is: {mpmath.nstr(total_result, 10, min_fixed=0, max_fixed=0)}"
    elif output_option[0] == 1:
        final_output = f"The full rounded up result is: {math.ceil(total_result)}"
    elif output_option[0] == 2:
        final_output = f"The full result is: {total_result}"
    elif output_option[0] == 3:
        final_output = f"The truncated result is: {str(total_result)[:101]}"

    print(final_output)

    if output_option[1]:  # save final result to file
        with open("calcd.txt", 'w') as f:
            f.write(final_output)
        print("The final result has been saved to 'calcd.txt'.")

    if output_option[2]:  # save all outputs to file
        with open("calcd_all.txt", 'w') as f:
            f.write('\n'.join(result_strings))
            f.write('\n' + final_output)
        print("The iterations and final result have been saved to 'calcd_all.txt'.")

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
'''

number = 0
operation = 0
precision = 15
output_option = (1, True, True, True)

calculate_result(v, number, operation, precision, output_option)
