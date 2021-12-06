

def simulate_fish(timer_count, day_from=1, day_to=80):
	for d in range(day_from, day_to + 1):
		zero_count = timer_count[0]
		for timer in range(1, len(timer_count)):
			timer_count[timer - 1] = timer_count[timer] 
			timer_count[timer] = 0

		timer_count[6] += zero_count
		timer_count[8] = zero_count
	return timer_count


def main():
	with open("input.txt") as f:
		initial_state = [int(n) for n in f.readline().split(",")]
		timer_count = [initial_state.count(n) for n in range(9)]
		
		part_one = simulate_fish(timer_count)
		print(f"Part one: {sum(part_one)}")
		part_two = simulate_fish(part_one, 81, 256)
		print(f"Part two: {sum(part_two)}")


if __name__ == "__main__":
	main()