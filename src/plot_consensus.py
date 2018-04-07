#!/usr/bin/env python3

from consensus import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def readAlignment(alignment_file):
	with open(alignment_file) as f:
		content = f.readlines()

	data_dict = {}
	ID = None

	for line in content:
		if line.startswith('>'):
			if ID is not None:
				data_dict[ID] = aligned_seq
			try:
				ID = line.split('|')[1]
			except IndexError:
				ID = line.split('>')[1]
			aligned_seq = []

		else:
			aligned_seq += list(line[:-1])

	return data_dict


def consensusPlot(image, consensus_freqs, color, x, y, width, height):
  '''Plot the most frequent amino acid at each position'''
  dpi = 150
  fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
  ax = fig.add_subplot(111)
  ax.grid(False)
  
  #plotArray = np.asarray(list(enumerate(consensus_freqs))).T
  x = list(range(consensus_freqs.shape[0]))
 
  ax.plot(x, consensus_freqs, '-', color=color)
 
  ax.fill_between(x, consensus_freqs, step="mid", alpha=.8, color=color)
 
  plt.tick_params(
      axis='x',          # changes apply to the x-axis
      which='both',      # both major and minor ticks are affected
      bottom='off',      # ticks along the bottom edge are off
      top='off',         # ticks along the top edge are off
      labelbottom='off') # labels along the bottom edge are off

  #plt.tight_layout()
  plt.savefig('consensus.png')

  #im = Image.open('consensus.png')
  #image.paste(im, (x, y))

 
