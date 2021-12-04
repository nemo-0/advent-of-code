import re
import copy

def play(numbers, boards):
	checked_numbers = []
	scores = []
	winners = []
	for number in numbers:
		checked_numbers.append(number)
		for board in boards:
			current_state = copy.deepcopy(board)
			current_state = [["marked" if n in checked_numbers else n for n in row] for row in board]

			if is_winner(current_state):
				sum_unmarked = sum([n for row in current_state for n in row if n != "marked"])
				if board not in winners:
					scores.append(number * sum_unmarked)
					winners.append(board)

	return scores


def is_winner(board):
	has_bingo = False
	if any([row.count("marked") == len(row) for row in board]):
		has_bingo = True

	columns = [[row[i] for row in board] for i in range(len(board))]
	if any([row.count("marked") == len(row) for row in columns]):
		has_bingo = True

	return has_bingo


def main():
	with open("input.txt") as f:
		numbers = [int(n) for n in f.readline().split(",")]
		boards = [[int(n) for n in re.split("\\s+", line.strip())] for line in f.readlines() if line.strip() != ""]
		boards = [[boards[n + i] for i in range(5)] for n in range(0, len(boards), 5)]

		scores = play(numbers, boards)
		print(f"Part one: {scores[0]}")
		print(f"Part two: {scores[-1]}")


if __name__ == "__main__":
	main()