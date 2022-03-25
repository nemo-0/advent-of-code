import re


def supports_TLS(sequence):
	abba_sequences = [(sequence[i:i+2] == sequence[i+2:i+4][::-1])
				 and (len(set(sequence[i:i+2])) == 2) for i in range(0, len(sequence) - 3)]

	return 1 if any(abba_sequences) else 0


def supports_SSL(hypernet_seqs, supernet_seqs):
	abas = [seq[i:i+3] for seq in supernet_seqs for i in range(len(seq) - 2) 
			if seq[i] == seq[i+2] and seq[i+1] != seq[i]]
	for aba in abas:
		for seq in hypernet_seqs:
			if re.findall(f"{aba[1]}{aba[0]}{aba[1]}", seq):
				return 1

	return 0


def count_ips_supporting_TLS(hypernet_seqs, supernet_seqs):
	ip_count = 0
	for i in range(len(supernet_seqs)):
		if any([supports_TLS(sequence) for sequence in hypernet_seqs[i]]):
			continue
		if any([supports_TLS(sequence) for sequence in supernet_seqs[i]]):
			ip_count += 1

	return ip_count


def count_ips_supporting_SSL(hypernet_seqs, supernet_seqs):
	ip_count = 0
	for i in range(0, len(supernet_seqs)):
		ip_count += supports_SSL(hypernet_seqs[i], supernet_seqs[i])

	return ip_count


def main():
	with open("input.txt") as f:
		ips = [line.strip() for line in f.readlines()]

		hypernet_seqs = [re.findall(r"\[(\w+)]", ip) for ip in ips]
		supernet_seqs = []
		for i in range(len(ips)):
			sequence = ips[i]
			for j in range(len(hypernet_seqs[i])):
				sequence = sequence.replace(f"[{hypernet_seqs[i][j]}]", " ")
			supernet_seqs.append(sequence.split())

		print(f"Part one: {count_ips_supporting_TLS(hypernet_seqs, supernet_seqs)}")
		print(f"Part two: {count_ips_supporting_SSL(hypernet_seqs, supernet_seqs)}")


if __name__ == "__main__":
	main()