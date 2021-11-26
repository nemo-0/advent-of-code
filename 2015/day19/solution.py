import re
import collections

reg = re.compile("(\\w+) => (\\w+)")
replacements = collections.defaultdict(list)
molecules = set()


def parse_data(line):
    result = re.match(reg, line)

    if result:
        molecule = result.group(1)
        replacement = result.group(2)

        replacements[molecule].append(replacement)


def generate_molecules(molecule):
    for m in replacements.keys():
        find_and_replace(molecule, m, replacements[m])


def find_and_replace(molecule, searched, all_replacements):
	found = molecule.find(searched)

	while found != -1:
		for replacement in all_replacements:
			new_molecule = molecule[:found] + replacement + molecule[found + len(searched):]
			molecules.add(new_molecule)

		found = molecule.find(searched, found + len(searched))


def step_count(molecule):
    # solution from https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
    tokens = sum(1 for c in molecule if c.isupper())
    parentheses = molecule.count("Rn") + molecule.count("Ar")
    comma = molecule.count("Y")
    return tokens - parentheses - 2 * comma - 1


def main():
    with open("input.txt") as f:
        contents = f.readlines()

        for line in contents:
            parse_data(line)

        medicine_molecule = contents[-1].strip()

        generate_molecules(medicine_molecule)
        print("Part one: ", len(molecules))
        print("Part two: ", step_count(medicine_molecule))


if __name__ == "__main__":
    main()

