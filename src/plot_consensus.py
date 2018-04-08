#!/usr/bin/env python3

from consensus import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageChops
import time

def consensusPlot(image, consensus_freqs, color, x, y, width, height):
  '''Plot the most frequent amino acid at each position'''
  dpi = 150
  fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
  #ax = fig.add_subplot(111)

  ax = plt.Axes(fig, [0., 0., 1., 1.])
  ax.set_axis_off()
  fig.add_axes(ax)
  #ax.grid(False)
  #ax.spines['right'].set_visible(False)
  #ax.spines['top'].set_visible(False)
  #ax.spines['bottom'].set_visible(False)
  #ax.set_facecolor('white')
  	
  xs = list(range(consensus_freqs.shape[0]))

  xmax = max(xs)
  ymax = np.argmax(consensus_freqs)

  plt.fill_between(xs, consensus_freqs, step="mid", alpha=.8, color=color)

  plt.tick_params(
      axis='x',          # changes apply to the x-axis
      which='both',      # both major and minor ticks are affected
      bottom='off',      # ticks along the bottom edge are off
      top='off',         # ticks along the top edge are off
      labelbottom='off') # labels along the bottom edge are off

  extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())

  plt.savefig('consensus.png', bbox_inches=extent, pad_inches=0)
  time.sleep(3)
  
  im = Image.open('consensus.png')
  bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
  diff = ImageChops.difference(im, bg)
  diff = ImageChops.add(diff, diff, 2.0, -100)
  bbox = diff.getbbox()
  cropped = im.crop(bbox)

  #cropped.show()
  
  cropped.paste(im, (x, y))

 
