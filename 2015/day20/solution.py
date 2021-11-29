import math

def get_divisors(house_number):
	divisors = [i for i in range(1, int(math.sqrt(house_number)) + 1) if house_number % i == 0]
	divisors.extend([house_number // i for i in divisors if i * i != house_number])

	return divisors


def get_house(input_presents, part_two=False):
	i = 0
	presents = 0
	while presents < input_presents:
		i += 1
		if part_two:
			presents = sum(d for d in get_divisors(i) if i // d <= 50) * 11
		else:
			presents = sum(get_divisors(i)) * 10 
		
	return i


def main():
	presents = 33100000
	print("Part one: ", get_house(presents))
	print("Part two: ", get_house(presents, True))


if __name__ == "__main__":
	main()