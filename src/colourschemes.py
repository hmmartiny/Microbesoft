#!/usr/bin/env python3

import seaborn as sns
import sys
from reduced_alphabets import *

def create_colour_scheme(alphabet, colourscheme="hls"):
    """
    Function that matches each 1-letter amino acid abbreviation with a hexadecimal 
    colour, depending on the standard reduced alphabets (see Peterson et al. 2009)
    used. Thus, amino acids with similar properties are coloured the same,
    depending on which similarity the user chooses
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732308/
    """
    # List of all available alphabets from pepdata library + the all / dna alphabet
    alphabets_available = ["all", "dna", "gbmr4", "sdm12", "hsdm17", "hp2", "murphy10", 
    "alex6", "aromatic2", "hp_vs_aromatic"]
    # If the alphabet is found
    if alphabet in alphabets_available:
        alphabet = eval(alphabet)
        alphabet_values = set(alphabet.values())
        colours = sns.color_palette(colourscheme, len(alphabet_values)).as_hex()
        for keys in alphabet.keys():
            alphabet[keys] = colours[alphabet[keys]]
    else:
        print("Colour input", alphabet, "not available.")
        sys.exit(1)
    return alphabet 
    
if __name__ == "__main__":
    colours = create_colour_scheme("all")
    print(colours)