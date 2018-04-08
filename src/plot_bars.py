#!/usr/bin/env python3

import matplotlib.pyplot as plt
from PIL import Image
import time
import numpy as np


def plot_bars(image, values, color, x, y, width, height):
    '''Plot the most frequent amino acid at each position'''
    dpi = 150
    fig = plt.figure(frameon=False, dpi=dpi, figsize=(width / dpi, height / dpi))
    ax = fig.add_subplot(1, 1, 1)
    plt.axis('off')
    plt.bar(np.arange(len(values)), values, color=color, width=1)
    plt.xlim(-0.5, len(values)-0.5)
    plt.ylim(0, 1)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('consensus.png', bbox_inches=extent, pad_inches=0, dpi=dpi)
    time.sleep(3)

    im = Image.open('consensus.png')
    # remove border from invisible axis
    im = im.crop((4, 4, im.width - 4, im.height - 4))
    # resize to the wanted size
    im = im.resize((width, height), Image.ANTIALIAS)
    image.paste(im, (x, y))