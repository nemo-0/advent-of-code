import hashlib


def find_password(door_id):
	password = ""
	hashcode = ""
	i = 0
	while len(password) < 8:
		new_value = f"{door_id}{i}".encode("utf-8")
		hashcode = hashlib.md5(new_value).hexdigest()

		if hashcode.startswith("00000"):
			# print(hashcode)
			password += hashcode[5]

		i += 1

	return password


def find_password_part_two(door_id):
	password = [None for _ in range(8)]
	hashcode = ""
	i = 0
	while None in password:
		new_value = f"{door_id}{i}".encode("utf-8")
		hashcode = hashlib.md5(new_value).hexdigest()
		i += 1

		if hashcode.startswith("00000"):
			index, char = hashcode[5], hashcode[6]
			
			if not index.isdigit():
				continue
			index = int(index)
			if index > 7 or password[index] is not None:
				continue
			else:
				password[index] = char

	return "".join(password)


def main():
	puzzle_input = "reyedfim"
	print(f"Part one: {find_password(puzzle_input)}")
	print(f"Part two: {find_password_part_two(puzzle_input)}")


if __name__ == "__main__":
	main()