#!/usr/bin/env python3

from consensus import *
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

#print(len(consensusFreq))

def consensusPlot(consensus_freqs, color):
  '''Plot the most frequent amino acid at each position'''
 
  plotArray = np.asarray(list(enumerate(consensus_freqs))).T
 
  ax.plot(plotArray[0,:], plotArray[1,:], '-', color=color)
 
  ax.fill_between(plotArray[0,:], plotArray[1,:], step="mid", alpha=.8, color=color)
 
  plt.tick_params(
      axis='x',          # changes apply to the x-axis
      which='both',      # both major and minor ticks are affected
      bottom='off',      # ticks along the bottom edge are off
      top='off',         # ticks along the top edge are off
      labelbottom='off') # labels along the bottom edge are off
 
  plt.show()
 
