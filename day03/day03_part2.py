
def find_gears_with_two_adjacent_integers(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Function to extract integers adjacent to a gear
    def extract_adjacent_integers(x, y, grid):
        adjacent_positions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        integers = []
        for ax, ay in adjacent_positions:
            if 0 <= ax < len(grid) and 0 <= ay < len(grid[ax]):
                char = grid[ax][ay]
                if char.isdigit():
                    # Build the full number if it's more than one digit
                    full_number = char
                    # Check left of the digit
                    lx = ay - 1
                    while lx >= 0 and grid[ax][lx].isdigit():
                        full_number = grid[ax][lx] + full_number
                        lx -= 1
                    # Check right of the digit
                    rx = ay + 1
                    while rx < len(grid[ax]) and grid[ax][rx].isdigit():
                        full_number = full_number + grid[ax][rx]
                        rx += 1
                    integers.append(int(full_number))
        return integers

    # Find gears and calculate the sum of the products
    total_sum = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == '*':
                integers = extract_adjacent_integers(x, y, lines)
                if len(integers) == 2:
                    total_sum += integers[0] * integers[1]

    return total_sum

total = find_gears_with_two_adjacent_integers('input')
print(total)
