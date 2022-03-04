import collections


def find_correct_message(messages, least_common=False):
	letter_counter = [collections.Counter([message[i] for message in messages]) for i in range(len(messages[0]))]

	funct = min if least_common else max
	correct_message = [funct(counter, key=counter.get) for counter in letter_counter]
	
	return "".join(correct_message)


def main():
	with open("input.txt") as f:
		messages = [line.strip() for line in f.readlines()]
		
		print(f"Part one: {find_correct_message(messages)}")
		print(f"Part two: {find_correct_message(messages, least_common=True)}")


if __name__ == "__main__":
	main()