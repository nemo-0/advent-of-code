import collections
import itertools
import functools


def play_with_deterministic_die(player1_pos, player2_pos):
	die = 1
	player1_score, player2_score = 0, 0
	player1 = [player1_score, player1_pos]
	player2 = [player2_score, player2_pos]
	curr_player = player1
	while player1[0] < 1000 and player2[0] < 1000:
		die += 3
		curr_player[1] = ((curr_player[1] + sum((die - 3, die - 2, die - 1)) - 1) % 10) + 1
		curr_player[0] += curr_player[1]
		
		curr_player = player1 if curr_player == player2 else player2

	return min(player1[0], player2[0]) * (die - 1)


@functools.cache
def play_with_quantum_die(player1_pos, player2_pos, player1_score, player2_score):
	rolls = collections.Counter(sum(roll) for roll in itertools.product([1, 2, 3], repeat=3))

	if player2_score >= 21:
		return (0, 1)

	games_won = [0, 0]
	for roll_sum, count in rolls.items():
		new_player1_pos = ((player1_pos + roll_sum - 1) % 10) + 1
		new_player1_score = player1_score + new_player1_pos
		wins2, wins1 = play_with_quantum_die(player2_pos, new_player1_pos, player2_score, new_player1_score)
		games_won[0] += (wins1 * count)
		games_won[1] += (wins2 * count)

	return games_won


def main():
	with open("input.txt") as f:
		player1_start_pos, player2_start_pos = int(f.readline().split()[-1]), int(f.readline().split()[-1])
	print(f"Part one: {play_with_deterministic_die(player1_start_pos, player2_start_pos)}")
	print(f"Part two: {max(play_with_quantum_die(player1_start_pos, player2_start_pos, 0, 0))}")


if __name__ == "__main__":
	main()