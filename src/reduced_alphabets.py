# This code is modified from the pepdata package reduced_alphabet.py
# by the Mount Sinai School of Medicine, under the Apache License Version 2.0

"""
Amino acid groupings from
'Reduced amino acid alphabets improve the sensitivity...' by
Peterson, Kondev, et al.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2732308/
"""

def dict_from_list(groups):
    aa_to_group = {}
    for i, group in enumerate(groups):
        for c in group:
            aa_to_group[c] = i
    return aa_to_group

gbmr4 = dict_from_list(["ADKERNTSQ", "YFLIVMCWH", "G", "P"])

sdm12 = dict_from_list([
    "A", "D", "KER", "N", "TSQ", "YF", "LIVM", "C", "W", "H", "G", "P"
])

hsdm17 = dict_from_list([
    "A", "D", "KE", "R", "N", "T", "S", "Q", "Y",
    "F", "LIV", "M", "C", "W", "H", "G", "P"
])

"""
Other alphabets originally from
http://bio.math-inf.uni-greifswald.de/viscose/html/alphabets.html,
which is currently unavailable, but incorporated in the pepdata package
"""

# hydrophilic vs. hydrophobic
hp2 = dict_from_list(["AGTSNQDEHRKP", "CMFILVWY"])

murphy10 = dict_from_list([
    "LVIM", "C", "A", "G", "ST", "P", "FYW", "EDNQ", "KR", "H"
])

alex6 = dict_from_list(["C", "G", "P", "FYW", "AVILM", "STNQRHKDE"])

aromatic2 = dict_from_list(["FHWY", "ADKERNTSQLIVMCGP"])

hp_vs_aromatic = dict_from_list(["H", "CMILV", "FWY", "ADKERNTSQGP"])


"""
Alphabets added by Microbesoft
"""
all = dict_from_list(["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
                     "N", "P", "Q", "R", "S", "T", "V", "W", "Y"])

dna = dict_from_list(["A", "T", "G", "C"])
