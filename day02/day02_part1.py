def is_possible(game, red, green, blue):
    for cubes in game:
        num_red = 0
        num_green = 0
        num_blue = 0
        for cube in cubes.split(","):
            if cube.strip().endswith("red"):
                num_red += int(cube.strip().split(" ")[0])
            elif cube.strip().endswith("green"):
                num_green += int(cube.strip().split(" ")[0])
            else:
                num_blue += int(cube.strip().split(" ")[0])
        if num_red > red or num_green > green or num_blue > blue:
            return False
    return True

games = [line.strip().split(":")[1] for line in open("input", "r").readlines()]

red = 12
green = 13
blue = 14

possible_games = []
for i, game in enumerate(games):
    if is_possible(game.split("; "), red, green, blue):
        possible_games.append(i + 1)

print(sum(possible_games))