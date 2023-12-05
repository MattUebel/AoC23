def parse_input(input_data):
    lines = input_data.strip().split('\n')
    games = {}
    for line in lines:
        game_id, game_data = line.split(': ')
        game_id = int(game_id.split(' ')[1])  # Extracting the game number
        subsets = game_data.split('; ')
        cube_counts = []
        for subset in subsets:
            counts = {'red': 0, 'green': 0, 'blue': 0}
            cubes = subset.split(', ')
            for cube in cubes:
                count, color = cube.split(' ')
                counts[color] = int(count)
            cube_counts.append(counts)
        games[game_id] = cube_counts
    return games

def calculate_minimum_cubes(games):
    min_cubes = {}
    for game_id, subsets in games.items():
        max_red = max_green = max_blue = 0
        for subset in subsets:
            max_red = max(max_red, subset['red'])
            max_green = max(max_green, subset['green'])
            max_blue = max(max_blue, subset['blue'])
        min_cubes[game_id] = {'red': max_red, 'green': max_green, 'blue': max_blue}
    return min_cubes

def calculate_power_sum(min_cubes):
    total_power = 0
    for cubes in min_cubes.values():
        power = cubes['red'] * cubes['green'] * cubes['blue']
        total_power += power
    return total_power

def main():
    # Reading input from file
    with open('input', 'r') as file:
        input_data = file.read()

    # Process the input data
    games = parse_input(input_data)

    # Calculate the minimum number of cubes for each game
    min_cubes = calculate_minimum_cubes(games)

    # Calculate the total power sum
    total_power_sum = calculate_power_sum(min_cubes)
    print(f"Total Power Sum: {total_power_sum}")

if __name__ == "__main__":
    main()
