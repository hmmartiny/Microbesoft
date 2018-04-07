#!/usr/bin/env python3
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont

AA_colors_cinema = {"A": "#c1ffc1", "B": "#ffffff", "C": "#50d433", "D": "#088446", "E": "#088446", "F": "#de94e3", 
                    "G": "#c1ffc1", "H": "#191996", "I": "#91b4ff", "J": "#ffffff", "K": "#ffa500", "L": "#91b4ff",
                    "M": "#91b4ff", "N": "#088446", "O": "#ffffff", "P": "#ffb6c1", "Q": "#088446", "R": "#ffa500",
                    "S": "#ce0000", "T": "#ce0000", "U": "#ffffff", "V": "#91b4ff", "W": "#de94e3", "X": "#ffffff",
                    "Y": "#de94e3", "Z": "#ffffff", "-": "#050505"}

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


def draw_sequences(sequences, font, AA_colors, size):
    """ Creates an PIL Image object with a table of aligned sequences on with coloring.
    :param sequences: a list of strings that are aligned sequences.
    :param font: an ImageFont object for drawing.
    :param AA_colors: a dict mapping a character to draw to its color.
    :param pad: space from letter edge to box edge.
    :return: an Image object with the result drawn on.
    """
    n_sequences = len(sequences)
    sequence_length = len(sequences[0])
    image_size = (sequence_length * size, n_sequences * size)
    img = Image.new('RGB', size=image_size, color='white')
    drawer = ImageDraw.Draw(img)
    
    for i_sequence, sequence in enumerate(sequences):
        for i_char, char in enumerate(sequence):
            draw_rectangle(drawer, i_char * size + size/2, i_sequence * size + size/2, size, color=AA_colors[char])
            draw_text(drawer, font, char, i_char * size + size/2, i_sequence * size + size/2)

    return img


def draw_headers(headers, font, size):
    n_headers = len(headers)
    headers_length = max(len(header) for header in headers)
    image_size = (headers_length * size, n_headers * size)
    img = Image.new('RGB', size=image_size, color='white')
    drawer = ImageDraw.Draw(img)
    
    max_width = 0
    for i_header, header in enumerate(headers):
        draw_text(drawer, font, header, 0, i_header * size + size/2, align='left')
        width, _ = drawer.textsize(header, font)
        if width > max_width:
            max_width = width
    
    img = img.crop((0, 0, max_width, img.height))
    return img


def image_hstack(images):
    width = sum(image.width for image in images)
    height = max(image.height for image in images)
    img = Image.new('RGB', size=(width, height))

    x = 0
    for image in images:
        img.paste(image, (x, 0))
        x += image.width
    
    return img


def draw(headers, sequences, font_path='etc/Menlo.ttc', fontsize=50, pad=20):
    
    font = ImageFont.truetype(font_path, size=fontsize)

    size = font.size + pad
    print("making sequence image")
    sequence_image = draw_sequences(sequences, font, AA_colors_cinema, size)
    print("making header image")
    header_image = draw_headers(headers, font, size)
    print("stacking")
    img = image_hstack([header_image, sequence_image])

    img.save("test.png")





