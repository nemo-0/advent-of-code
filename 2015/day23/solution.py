

registers = {"a": 0, "b": 0}

def hlf(r):
	registers[r] /= 2
	return 1


def tpl(r):
	registers[r] *= 3
	return 1


def inc(r):
	registers[r] += 1
	return 1


def jmp(offset):
	return offset


def jie(r, offset):
	if registers[r] % 2 == 0:
		return offset
	else:
		return 1


def jio(r, offset):
	if registers[r] == 1:
		return offset
	else: 
		return 1


def run(program):
	i = 0
	while i < len(program):
		instruction = program[i].split(' ')
		name = instruction[0]

		if name == "hlf":
			i += hlf(instruction[1])
		elif name == "tpl":
			i += tpl(instruction[1])
		elif name == "inc":
			i += inc(instruction[1])
		elif name == "jmp":
			i += jmp(int(instruction[1]))
		elif name == "jie":
			i += jie(instruction[1].strip(","), int(instruction[2]))
		elif name == "jio":
			i += jio(instruction[1].strip(","), int(instruction[2]))


def main():
	with open("input.txt") as f:
		contents = [l.strip() for l in f.readlines()]

		run(contents)
		print("Part one: ", registers["b"])

		registers["a"] = 1
		registers["b"] = 0
		run(contents)
		print("Part two: ", registers["b"])


if __name__ == "__main__":
	main()