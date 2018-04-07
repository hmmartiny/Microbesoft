#!/usr/bin/env python3
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont

font_path = '../etc/cmunrm.ttf'


def draw_text(drawer, font, text, x, y, size, text_color="black", bg_color="blue"):
    """Draws centered text with background rectangle."""
    width, height = drawer.textsize(text, font=font)
    drawer.rectangle(((x - size/2, y - size/2), (x + size/2, y + size/2)), fill=bg_color)
    drawer.text((x - width/2, y - height/2), text, fill=text_color, font=font)




def draw(sequences):
    n_sequences = len(sequences)
    sequence_length = len(sequences[0])

    fontsize = 60
    size = 70
    image_size = (sequence_length * size, n_sequences * size)
    img = Image.new('RGB', size=image_size, color='white')
    drawer = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, size=fontsize)
     
    for i_sequence, sequence in enumerate(sequences):
        for i_char, char in enumerate(sequence):
            draw_text(drawer, font, char, i_char * size + size/2, i_sequence * size + size/2, size)

    img.save("test.png")
    
    




