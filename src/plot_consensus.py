#!/usr/bin/env python3

from consensus import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def consensusPlot(image, consensus_freqs, color, x, y, width, height):
  '''Plot the most frequent amino acid at each position'''
  dpi = 150
  fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
  ax = fig.add_subplot(111)
  #ax.grid(False)
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['bottom'].set_visible(False)
  ax.set_aspect(2)
  	
  x = list(range(consensus_freqs.shape[0]))

 
  ax.fill_between(x, consensus_freqs, step="mid", alpha=.8, color=color)
 
  plt.tick_params(
      axis='x',          # changes apply to the x-axis
      which='both',      # both major and minor ticks are affected
      bottom='off',      # ticks along the bottom edge are off
      top='off',         # ticks along the top edge are off
      labelbottom='off') # labels along the bottom edge are off

  plt.tight_layout()
  plt.savefig('consensus.png', bbox_inches="tight", pad_inches=0)
  
  im = Image.open('consensus.png')
  image.paste(im, (x, y))

 
