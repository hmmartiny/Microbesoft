#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from plot_consensus import consensusPlot

AA_colors_cinema = {"A": "#c1ffc1", "B": "#ffffff", "C": "#50d433", "D": "#088446", "E": "#088446", "F": "#de94e3", 
                    "G": "#c1ffc1", "H": "#191996", "I": "#91b4ff", "J": "#ffffff", "K": "#ffa500", "L": "#91b4ff",
                    "M": "#91b4ff", "N": "#088446", "O": "#ffffff", "P": "#ffb6c1", "Q": "#088446", "R": "#ffa500",
                    "S": "#ce0000", "T": "#ce0000", "U": "#ffffff", "V": "#91b4ff", "W": "#de94e3", "X": "#ffffff",
                    "Y": "#de94e3", "Z": "#ffffff"}

def draw_rectangle(drawer, x, y, size, color="blue"):
    """Draws centered text with background rectangle."""
    drawer.rectangle(((x - size/2, y - size/2), (x + size/2, y + size/2)), fill=color)


def draw_text(drawer, font, text, x, y, color="black", align='center'):
    """Draws centered text with background rectangle."""
    width, height = drawer.textsize(text, font=font)
    if align == 'center':
        x -= width / 2
    y -= height / 2
    drawer.text((x, y), text, fill=color, font=font)


def draw_numbering(drawer, interval, font, size, x=0, y=0):
    interval = np.arange(interval[0], interval[1])
    for i in range(len(interval)):
        if interval[i] % 5 != 0: continue
        draw_x = x + i * size
        draw_y = y + size/2
        draw_text(drawer, font, str(interval[i]), draw_x, draw_y, align='left')


def draw_sequences(drawer, sequences, interval, font, AA_colors, size, x=0, y=0):
    """ Creates an PIL Image object with a table of aligned sequences on with coloring.
    :param sequences: a list of strings that are aligned sequences.
    :param font: an ImageFont object for drawing.
    :param AA_colors: a dict mapping a character to draw to its color.
    :param pad: space from letter edge to box edge.
    :return: an Image object with the result drawn on.
    """
    for i_sequence, sequence in enumerate(sequences):
        for i_char, char in enumerate(sequence[interval[0]:interval[1]]):
            char = char.upper()
            color = AA_colors.get(char, 'white')
            draw_x = x + i_char * size + size/2
            draw_y = y + i_sequence * size + size/2
            draw_rectangle(drawer, draw_x, draw_y, size, color=color)
            draw_text(drawer, font, char, draw_x, draw_y)


def draw_headers(drawer, headers, font, size, x=0, y=0):
    """:return width so we can draw the sequences after this."""
    max_width = 0
    for i_header, header in enumerate(headers):
        draw_text(drawer, font, header, x, y + i_header * size + size/2, align='left')
        width, _ = drawer.textsize(header, font)
        if width > max_width:
            max_width = width
    
    return max_width


def image_hstack(images):
    width = sum(image.width for image in images)
    height = max(image.height for image in images)
    img = Image.new('RGB', size=(width, height))

    x = 0
    for image in images:
        img.paste(image, (x, 0))
        x += image.width
    
    return img


def draw(headers, sequences, consensus_frequencies, font_path='etc/Menlo.ttc', fontsize=30, pad=10, max_width=200):
    font = ImageFont.truetype(font_path, size=fontsize)
    size = font.size + pad
    n_sequences = len(sequences)
    sequence_length = len(sequences[0])
    n_parts = sequence_length // max_width + 1
    sequences_height = n_sequences * size
    numbering_height = 1 * size
    frequency_height = 3 * size
    part_height = sequences_height + numbering_height + frequency_height
    image_size = (min(sequence_length, max_width) * size, part_height * n_parts)
    img = Image.new('RGB', size=image_size, color='white')
    drawer = ImageDraw.Draw(img)
    
    for i_part in range(n_parts):
        print("drawing part", i_part)
        draw_y = i_part * part_height
        header_width = draw_headers(drawer, headers, font, size, y=draw_y + numbering_height)
        sequence_interval = [int(i_part*max_width), int(min((i_part+1)*max_width, sequence_length))]
        draw_numbering(drawer, sequence_interval, font, size, x=header_width, y=draw_y)
        draw_sequences(drawer, sequences, sequence_interval, font, AA_colors_cinema, size, x=header_width, y=draw_y + numbering_height)
        part_frequencies = np.asarray(consensus_frequencies)[sequence_interval[0]:sequence_interval[1]]
        frequency_width = (sequence_interval[1] - sequence_interval[0]) * size
        consensusPlot(img, part_frequencies, color='black', x=header_width, y=draw_y + sequences_height + numbering_height, width=frequency_width, height=frequency_height)

    img.save("test.png")





