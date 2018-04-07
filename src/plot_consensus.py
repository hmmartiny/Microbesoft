#!/usr/bin/env python3

from consensus import *
from visualize import *
import matplotlib.pyplot as plt
import numpy as np

def readAlignment(alignment_file):
	with open(alignment_file) as f:
		content = f.readlines()

	data_dict = {}
	ID = None

	for line in content:
		if line.startswith('>'):
			if ID is not None:
				data_dict[ID] = aligned_seq
			
			ID = line.split('|')[1]
			aligned_seq = []

		else:
			aligned_seq += list(line[:-1])

	return data_dict

alnSequences = readAlignment('../data/aln_picorna.txt')

consensusSeq, consensusFreq = consensus(alnSequences.values())

findConsensus(alnSequences.values())
#print(len(consensusFreq))

fig = plt.figure()
ax = fig.add_subplot(111)
plotArray = np.asarray(list(enumerate(consensusFreq))).T
ax.plot(plotArray[0,:], plotArray[1,:], '-')
ax.fill_between(plotArray[0,:], plotArray[1,:], step="mid", alpha=.2)
ax.set_xticks(plotArray[0, :], list(consensusSeq))
#plt.show()
