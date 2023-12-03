def sum_calibration_values_from_file(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Find the first digit
            first_digit = next((char for char in line if char.isdigit()), None)
            # Find the last digit (reversing the string)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)

            # If both digits are found, add their combination to the total
            if first_digit and last_digit:
                calibration_value = int(first_digit + last_digit)
                total += calibration_value

    return total

# Usage
total = sum_calibration_values_from_file('input')
print("Total calibration value:", total)
