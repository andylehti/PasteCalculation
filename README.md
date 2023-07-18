# PasteCalc
PasteCalc is a personal utility for Python environments that allows you to calculate values by pasting them into a string array. This utility is not meant to be called as a script as it does not have meaningful input options.

## Getting Started

To use this script, follow the instructions below:

1. Ensure you have Python installed on your system.
2. Install the `mpmath` library by running the command: `pip install mpmath`.
3. Setup a Python3 environment or use a Python based notebook (you may also call the script, but the values will have to be edited in the script every time)

## Usage

1. Open the script in a Python editor or IDE.
2. Modify the input parameters as needed:
   - `v`: Paste the values you want to use for calculations between the specified lines.
   - `number`: Set the initial number for calculations. If set to 0, the script will use the first value from the `v` list.
   - `operation`: Choose the operation to perform:
     - 0: Addition
     - 1: Subtraction
     - 2: Multiplication
     - 3: Division
   - `precision`: Adjust the precision of the calculations (optional).
   - `print_iterations`: Set to `True` to print the result after each iteration.
   - `output_option`: Choose the output option:
     - 0: Partial scientific notation
     - 1: Full result
     - 2: Save to file
     - 3: Partial truncated result

3. Run the script. The calculated result will be displayed based on the chosen output option.

**Note:** If you choose output option 2 (save to file), the result will be saved in a file named `calcd.txt`.

## Usage

1. Open the `PasteCalc.py` script in a Python editor or IDE.
2. Copy the values you want to calculate.
3. Replace the placeholder lines in the string in the `v` variable with the copied values.
4. Run the script. No need to format, no need to add a tab, no need to add a comma at the end.

The calculated result will be displayed based on the specified operation and output options.

## Script

```python
import mpmath

# Paste the values between the third line
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

number = 0  # addition, subtraction, multiplication, and division will add to, subtract from, multiply by, and divide by each in the array respectively
operation = 2  # operation: 0 = "add", 1 = "subtract", 2 = "multiply", 3 = "divide"
precision = 15  # dynamic precision (adjust as needed)
print_iterations = False  # option to print the result after each iteration
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
```

## License

This project is licensed under the [MIT License](LICENSE).
