

def get_power_consumption(numbers):
	bits = len(numbers[0])
	gamma_rate = ""
	epsilon_rate = ""

	for b in range(bits):
		column = [numbers[n][b] for n in range(len(numbers))]
		ones, zeros = column.count("1"), column.count("0")
		
		gamma_rate += "1" if ones > zeros else "0"
		epsilon_rate += "1" if ones < zeros else "0"

	return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_rating(numbers, type):
	bits = len(numbers[0])

	for b in range(bits):
		if len(numbers) == 1:
			break

		column = [numbers[n][b] for n in range(len(numbers))]
		ones, zeros = column.count("1"), column.count("0")

		if type == "oxygen":
			bit = "1" if ones >= zeros else "0"
		elif type == "co2":
			bit = "1" if ones < zeros else "0"

		numbers = [numbers[n] for n in range(len(numbers)) if numbers[n][b] == bit]

	return int(numbers[0], 2)


def get_life_support(numbers):
	oxygen_rating = get_rating(numbers, "oxygen")
	co2_rating = get_rating(numbers, "co2")

	return oxygen_rating * co2_rating

	
def main():
	with open("input.txt") as f:
		contents = [n.strip() for n in f.readlines()]

		print(f"Part one: {get_power_consumption(contents)}")
		print(f"Part two: {get_life_support(contents)}")


if __name__ == "__main__":
	main()