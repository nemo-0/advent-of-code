import itertools
import collections

weapons = {"Dagger": [8, 4, 0], 
			"Shortsword": [10, 5, 0], 
			"Warhammer": [25, 6, 0], 
			"Longsword": [40, 7, 0], 
			"Greataxe": [74, 8, 0]}

armor = {"Leather": [13, 0, 1], 
		"Chainmail": [31, 0, 2],
		"Splintmail": [53, 0, 3],
		"Bandedmail": [75, 0, 4],
		"Platemail": [102, 0, 5]}

rings = {"Damage +1": [25, 1, 0],
		"Damage +2": [50, 2, 0],
		"Damage +3": [100, 3, 0],
		"Defense +1": [20, 0, 1],
		"Defense +2": [40, 0, 2],
		"Defense +3": [80, 0, 3]}

boss_stats = {}
possible_stats = []

def get_boss_stats(file):
	with open(file) as f:
		for line in f:
			(key, val) = line.split(":")
			boss_stats[key] = int(val)
 

def get_loadouts():
	all_items = []
	for d in (weapons, armor, rings):
		all_items.extend(d.keys())

	for i in range(2, 5):
		for loadout in itertools.combinations(all_items, i):
			bought_weapons = {}
			bought_armor = {}
			bought_rings = {}

			for item in loadout:
				if item in weapons:
					bought_weapons[item] = weapons[item]
				elif item in armor:
					bought_armor[item] = armor[item]
				else:
					bought_rings[item] = rings[item]

			if is_valid_loadout(bought_weapons, bought_armor, bought_rings):
				player_stats = get_player_stats(bought_weapons | bought_armor | bought_rings)
				possible_stats.append(player_stats)
				

def is_valid_loadout(bought_weapons, bought_armor, bought_rings):
	return len(bought_weapons) == 1 and len(bought_armor) <= 1 and len(bought_rings) <= 2


def get_player_stats(player_loadout):
	gold = 0
	damage = 0
	armor = 0

	for stats in player_loadout.values():
		gold += stats[0]
		damage += stats[1]
		armor += stats[2]

	return (gold, damage, armor)


def is_boss_defeated(player_stats):
	damage_to_boss = player_stats[1] - boss_stats["Armor"] or 1
	damage_to_player = boss_stats["Damage"] - player_stats[2] or 1
	boss_hp = boss_stats["Hit Points"]
	player_hp = 100

	while True:
		boss_hp -= damage_to_boss
		if boss_hp <= 0:
			return True

		player_hp -= damage_to_player
		if player_hp <= 0:
			return False

	# player_attacks = boss_hp // damage_to_boss
	# boss_attacks = player_hp // damage_to_player 

	# return player_attacks < boss_attacks


def find_best_loadout():
	gold_per_winning_loadout = []
	for stat in possible_stats:
		if is_boss_defeated(stat):
			gold_per_winning_loadout.append(stat[0])

	return min(gold_per_winning_loadout)


def find_worst_loadout():
	gold_per_losing_loadout = []
	for stat in possible_stats:
		if not is_boss_defeated(stat):
			gold_per_losing_loadout.append(stat[0])

	return max(gold_per_losing_loadout)


def main():
	get_boss_stats("input.txt")
	get_loadouts()

	print("Part one: ", find_best_loadout())
	print("Part two: ", find_worst_loadout())


if __name__ == "__main__":
	main()