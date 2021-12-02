

def parse_commands(lines, part_two=False):
	commands = {"forward": 0, "down": 0, "up": 0}
	depth_part_two = 0
	for line in lines:
		command, units = line.split(" ")
		commands[command] += int(units)

		if part_two and command == "forward":
			depth_part_two += int(units) * (commands["down"] - commands["up"]) 

	return commands, depth_part_two


def main():
	with open("input.txt") as f:
		contents = f.readlines()

		commands, _ = parse_commands(contents)
		part_one = commands["forward"] * (commands["down"] - commands["up"])
		print(f"Part one: {part_one}")

		commands, depth = parse_commands(contents, True)
		part_two = commands["forward"] * depth
		print(f"Part two: {part_two}")


if __name__ == "__main__":
	main()