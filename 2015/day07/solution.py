import re


re_store = re.compile("(\\w+) -> (\\w+)")
re_and = re.compile("(\\w+) AND (\\w+) -> (\\w+)")
re_lshift = re.compile("(\\w+) LSHIFT (\\w+) -> (\\w+)")
re_not = re.compile("NOT (\\w+) -> (\\w+)")
re_or = re.compile("(\\w+) OR (\\w+) -> (\\w+)")
re_rshift = re.compile("(\\w+) RSHIFT (\\w+) -> (\\w+)")

wires = {}

def store(arg, wire_to):
	try:
		wires[wire_to] = int(arg)
	except ValueError:
		wires[wire_to] = wires[arg]

def bitwise_and(arg1, arg2, wire_to):
	if arg1.isdigit():
		wires[wire_to] = int(arg1) & wires.get(arg2)
	elif arg2.isdigit():
		wires[wire_to] = wires.get(arg1) & int(arg2)
	else:
		wires[wire_to] = wires.get(arg1) & wires.get(arg2)


def left_shift(arg1, arg2, wire_to):
	wires[wire_to] = wires.get(arg1) << int(arg2)


def bitwise_complement(arg1, wire_to):
	bin_arg1 = bin(wires[arg1])[2:].zfill(16)
	result = ""
	for b in bin_arg1:
		if b == "0":
			result += "1"
		else:
			result += "0"

	wires[wire_to] = int(result, 2)

def bitwise_or(arg1, arg2, wire_to):
	if arg1.isdigit():
		wires[wire_to] = int(arg1) | wires.get(arg2)
	elif arg2.isdigit():
		wires[wire_to] = wires.get(arg1) | int(arg2)
	else:
		wires[wire_to] = wires.get(arg1) | wires.get(arg2)


def right_shift(arg1, arg2, wire_to):
	wires[wire_to] = wires.get(arg1) >> int(arg2)


command_func = {"store": [re_store, store],
				"bitwise_and": [re_and, bitwise_and],
				"left_shift": [re_lshift, left_shift],
				"bitwise_complement": [re_not, bitwise_complement],
				"bitwise_or": [re_or, bitwise_or],
				"right_shift": [re_rshift, right_shift]}


def apply(line, wire_a=None):
	if wire_a is not None:
		wires["b"] = wire_a

	for action in command_func.keys():
		result = re.match(command_func[action][0], line)

		if result:
			return command_func[action][1](*result.groups())


def run(file, part_two=None):
	with open(file) as f:
		contents = f.readlines()

		while contents:
			completed = []
			for line in contents:
				try:
					apply(line, part_two)
					completed.append(line)
				except (TypeError, KeyError):
					continue

			for c in completed:
				contents.remove(c)


def main():
		run("input.txt")
		
		print("Part one: ", wires["a"])

		wire_a = wires["a"]
		wires.clear()
		wires["b"] = wire_a

		run("input.txt", wire_a)
		print("Part two: ", wires["a"])


if __name__ == "__main__":
	main()
