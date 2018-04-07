#!/user/bin/python3

import matplotlib.pyplot as plt

with open('../data/aln_picorna.txt') as f:
	content = f.readlines()

data_dict = {}
ID = None

hydrophobic = ['A', 'I', 'L', 'M', 'F', 'V', 'P', 'G']
polar = ['Q', 'N', 'H', 'S', 'T', 'Y', 'C', 'W']
charged = ['R', 'K', 'D', 'E']


for line in content:
	if line.startswith('>'):
		if ID is not None:
			data_dict[ID] = aligned_seq
		
		ID = line.split('|')[1]
		aligned_seq = []

	else:
		aligned_seq += list(line[:-1])

# plotting
fig, ax = plt.subplots(figsize=(15, 10))
ax.grid(True)


for i, (ID, aln_seq) in enumerate(data_dict.items()):
	if i < 1:
		print(i + 1, "/", len(data_dict), end='\r')
		for j, aa in enumerate(aln_seq):
			if aa in hydrophobic:
				ax.scatter(j+1, i+1, color='blue', marker='s')
			elif aa in polar:
				ax.scatter(j+1, i+1, color='red', marker='s')
			elif aa in charged:
				ax.scatter(j+1, i+1, color='green', marker='s')
			else:
				ax.scatter(j+1, i+1, color='black', marker='s')
	else:
		break

plt.show()