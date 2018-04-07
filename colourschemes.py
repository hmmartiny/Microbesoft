#!/usr/bin/env python3

from pepdata.reduced_alphabet import *
import seaborn as sns
import sys

def create_colour_scheme(alphabet, colourscheme="hls"):
    """
    Function that matches each 1-letter amino acid abbreviation with a hexadecimal 
    colour, depending on the standard reduced alphabets (see Peterson et al. 2009)
    used. Thus, amino acids with similar properties are coloured the same,
    depending on which similarity the user chooses
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732308/
    """
    # Create a non-reduced alphabet dictionary (1 letter abbreviation == itself)
    all = dict(zip(gbmr4.keys(), gbmr4.keys()))
    # List of all reduced alphabets from pepdata library
    alphabets_available = ["all", "gbmr4", "sdm12", "hsdm17", "hp2", "murphy10", 
    "alex6", "aromatic2", "hp_vs_aromatic"]
    # If the alphabet is found
    if alphabet in alphabets_available:
        alphabet = eval(alphabet)
        alphabet_values = set(alphabet.values())
        colours = sns.color_palette(colourscheme, len(alphabet_values)).as_hex()
        translation_dict = dict(zip(alphabet_values, colours))
        for keys in alphabet.keys():
            alphabet[keys] = translation_dict[alphabet[keys]]
    else:
        print("Colour input", userinput, "not available.")
        sys.exit(1)
    return alphabet 
    
if __name__ == "__main__":
    colours = create_colour_scheme("all")
    print(colours)