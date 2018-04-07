#!/usr/bin/env python3
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont



def draw_text(drawer, font, text, x, y, size, text_color="black", bg_color="blue"):
    """Draws centered text with background rectangle."""
    width, height = drawer.textsize(text, font=font)
    drawer.rectangle(((x - size/2, y - size/2), (x + size/2, y + size/2)), fill=bg_color)
    drawer.text((x - width/2, y - height/2), text, fill=text_color, font=font)


def draw_table(sequences, font, AA_colors, pad=10):
    """ Creates an PIL Image object with a table of aligned sequences on with coloring.
    :param sequences: a list of strings that are aligned sequences.
    :param font: an ImageFont object for drawing.
    :param AA_colors: a dict mapping a character to draw to its color.
    :param pad: space from letter edge to box edge.
    :return: an Image object with the result drawn on.
    """
    size = font.size - pad
    n_sequences = len(sequences)
    sequence_length = len(sequences[0])
    image_size = (sequence_length * size, n_sequences * size)
    img = Image.new('RGB', size=image_size, color='white')
    drawer = ImageDraw.Draw(img)
    
    for i_sequence, sequence in enumerate(sequences):
        for i_char, char in enumerate(sequence):
            draw_text(drawer, font, char, i_char * size + size/2, i_sequence * size + size/2, size, bg_color=AA_colors[char])

    return img


def draw(sequences, font_path='../etc/Menlo.ttc', fontsize = 60, pad=10):
    
    font = ImageFont.truetype(font_path, size=fontsize)

    AA_colors = {'A': 'red', 'R': 'green', 'N': 'blue'}
    
    img = draw_table(sequences, font, AA_colors, pad)

    img.save("test.png")
    
    




