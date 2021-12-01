import random
import copy

boss_stats = {}
player_stats = {"Hit Points": 50, "Damage": 0, "Armor": 0, "Mana": 500, "Mana Spent": 0}
all_spells = {"Magic Missile": {"Cost": 53, "Damage": 4, "Heal": 0, "Armor": 0, "Mana": 0, "Turns": 0},
              "Drain": {"Cost": 73, "Damage": 2, "Heal": 2, "Armor": 0, "Mana": 0, "Turns": 0},
              "Shield": {"Cost": 113, "Damage": 0, "Heal": 0, "Armor": 7, "Mana": 0, "Turns": 6},
              "Poison": {"Cost": 173, "Damage": 3, "Heal": 0, "Armor": 0, "Mana": 0, "Turns": 6},
              "Recharge": {"Cost": 229, "Damage": 0, "Heal": 0, "Armor": 0, "Mana": 101, "Turns": 5}}
min_mana = 1000000


def get_boss_stats(file):
    with open(file) as f:
        for line in f:
            (key, val) = line.split(":")
            boss_stats[key] = int(val)


def player_turn(current_spells, curr_boss_stats, curr_player_stats, hard_mode=False):
    if hard_mode:
        curr_player_stats["Hit Points"] -= 1

        if curr_player_stats["Hit Points"] <= 0:
            return None

    spells, curr_boss_stats, curr_player_stats = apply_effects(current_spells, curr_boss_stats, curr_player_stats)

    if is_victory(curr_boss_stats, curr_player_stats):
        return None

    spells, curr_player_stats = get_next_spell(spells, curr_player_stats)

    return [spells, curr_boss_stats, curr_player_stats]


def boss_turn(current_spells, curr_boss_stats, curr_player_stats):
    spells, curr_boss_stats, curr_player_stats = apply_effects(current_spells, curr_boss_stats, curr_player_stats)

    if is_victory(curr_boss_stats, curr_player_stats):
        return None

    damage = curr_boss_stats["Damage"] - curr_player_stats["Armor"] or 1
    curr_player_stats["Hit Points"] -= damage

    return [spells, curr_boss_stats, curr_player_stats]


def apply_effects(current_spells, curr_boss_stats, curr_player_stats):
    to_remove = []
    for spell in current_spells.keys():
        curr_boss_stats["Hit Points"] -= all_spells[spell]["Damage"]
        curr_player_stats["Hit Points"] += all_spells[spell]["Heal"]
        curr_player_stats["Mana"] += all_spells[spell]["Mana"]

        if spell == "Shield":
            curr_player_stats["Armor"] = all_spells[spell]["Armor"]

        current_spells[spell]["Turns"] -= 1
        if current_spells[spell]["Turns"] <= 0:
            to_remove.append(spell)
            if spell == "Shield":
                curr_player_stats["Armor"] = 0

    for k in to_remove:
        current_spells.pop(k)

    return current_spells, curr_boss_stats, curr_player_stats


def get_next_spell(current_spells, curr_player_stats):
    possible_spells = {k: v.copy() for k, v in all_spells.items() if k not in current_spells.keys()}

    no_spell_chosen = True
    while no_spell_chosen and len(possible_spells) > 0:
        next_spell = random.choice(list(possible_spells.keys()))
        possible_spells.pop(next_spell)

        if all_spells[next_spell]["Cost"] > curr_player_stats["Mana"]:
            continue

        curr_player_stats["Mana"] -= all_spells[next_spell]["Cost"]
        curr_player_stats["Mana Spent"] += all_spells[next_spell]["Cost"]

        current_spells[next_spell] = all_spells[next_spell].copy()
        no_spell_chosen = False

    return current_spells, curr_player_stats


def is_victory(curr_boss_stats, curr_player_stats):
    if curr_boss_stats["Hit Points"] <= 0:
        mana_spent = curr_player_stats["Mana Spent"]

        global min_mana
        if mana_spent < min_mana:
            min_mana = mana_spent

        return True
    return False


def play(hard_mode=False):
    current_spells = {}
    curr_boss_stats = copy.deepcopy(boss_stats)
    curr_player_stats = copy.deepcopy(player_stats)

    while True:

        turn_result = player_turn(current_spells, curr_boss_stats, curr_player_stats, hard_mode)

        if turn_result is None:
            return

        current_spells, curr_boss_stats, curr_player_stats = turn_result

        turn_result = boss_turn(current_spells, curr_boss_stats, curr_player_stats)

        if turn_result is None:
            return

        current_spells, curr_boss_stats, curr_player_stats = turn_result

        if curr_player_stats["Hit Points"] <= 0:
            return


def main():
    get_boss_stats("input.txt")

    # Hack solution, might have to rerun the program a couple times to get the right answer.
    for _ in range(1000000):
        play()

    global min_mana

    # Part one: 1824
    print("Part one: ", min_mana)

    min_mana = 1000000
    for _ in range(1000000):
        play(True)

    # Part two: 1937
    print("Part two: ", min_mana)


if __name__ == "__main__":
    main()