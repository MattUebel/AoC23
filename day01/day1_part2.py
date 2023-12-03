import re

def main():
    data = [line.strip() for line in open('input', 'r').readlines()]
    
    # Regular expression to find all occurrences of spelled-out numbers and digits
    number_word_re = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    number_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                    "six": 6, "seven": 7, "eight": 8, "nine": 9}

    # Function to replace spelled-out numbers with digits
    def replace_spelled_numbers(line):
        matches = number_word_re.findall(line)
        return [number_words.get(match, match) for match in matches]

    # Calculate the sum of all calibration values
    total_sum = 0
    for line in data:
        digits = replace_spelled_numbers(line)
        total_sum += int(str(digits[0]) + str(digits[-1]))

    return total_sum

# Execute the script and print the total calibration value
total_calibration_value = main()
print("Total calibration value:", total_calibration_value)
