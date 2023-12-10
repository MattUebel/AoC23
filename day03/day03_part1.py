def sum_part_numbers(filename):
    with open(filename, 'r') as file:
        schematic = file.readlines()

    # Helper function to check if a given position has a symbol
    def has_symbol(i, j):
        # symbols are non-digit characters except for a period
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '<', '>', '/', '?', '`', '~']
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= i+di < len(schematic) and 0 <= j+dj < len(schematic[0]) and schematic[i+di][j+dj] in symbols:
                    return True
        return False

    total = 0
    for i, line in enumerate(schematic):
        j = 0
        while j < len(line):
            if line[j].isdigit():
                num_end = j + 1
                while num_end < len(line) and line[num_end].isdigit():
                    num_end += 1

                number = int(line[j:num_end])
                # check if any digit of the number has a symbol adjecent to it
                if any(has_symbol(i, j) for j in range(j, num_end)):
                    total += number

                j = num_end
            else:
                j += 1

    return total

# Example usage
print(sum_part_numbers('input'))
