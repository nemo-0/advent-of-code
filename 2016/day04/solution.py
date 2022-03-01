import collections
from string import ascii_lowercase as ALPHABET


def is_real_room(room):
	checksum = room[-1]
	letters = sorted([letter for name in room[:-2] for letter in name])
	letter_count = collections.Counter(letters)
	most_common = "".join(pair[0] for pair in letter_count.most_common(5))

	return most_common == checksum


def sum_ids(rooms):
	id_sum = 0
	for room in rooms:
		sector_id = room[-2]
		if is_real_room(room):
			id_sum += sector_id

	return id_sum


def find_id(rooms):
	for room in rooms:
		if is_real_room(room):
			key = room[-2] % len(ALPHABET)
			trantab = str.maketrans(ALPHABET, ALPHABET[key:] + ALPHABET[:key])
			encrypted = " ".join(room[:-2])
			decrypted = encrypted.translate(trantab)
			
			if "northpole" in decrypted:
				return room[-2]
				
	return None


def main():
	with open("input.txt") as f:
		rooms = []
		for line in f.readlines():
			splitted = line.strip().split("-")
			sector_id, checksum = splitted[-1].split("[")
			checksum = checksum[:-1]
			room = splitted[:-1] + [int(sector_id), checksum]
			rooms.append(room)

		print(f"Part one: {sum_ids(rooms)}")
		print(f"Part two: {find_id(rooms)}")
	

if __name__ == "__main__":
	main()