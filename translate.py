#!/usr/bin/env python3
import sys

def translate_dna_to_aa(dna_sequence, search_for_startcodon = True):
    """
    Function that translates DNA sequence into amino acids. 
    It searches for the first ATG startcodon if search_for_startcodon is True,
    otherwise it assumes that the first base of the sequence is the start of 
    the open reading frame.
    Translation stops when the first stopcodon in the right reading frame is
    found after the startcodon.
    """
    # Create a translation table to convert a DNA codon into an amino acid
    amino_acid_table = {'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'CTT': 'L', 'CTC': 'L',
                        'CTA': 'L', 'CTG': 'L', 'TTA': 'L', 'TTG': 'L', 'GTT': 'V',
                        'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'TTT': 'F', 'TTC': 'F',
                        'ATG': 'M', 'TGT': 'C', 'TGC': 'C', 'GCT': 'A', 'GCC': 'A',
                        'GCA': 'A', 'GCG': 'A', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
                        'GGG': 'G', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'TCT': 'S',
                        'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
                        'TAT': 'Y', 'TAC': 'Y', 'TGG': 'W', 'CAA': 'Q', 'CAG': 'Q',
                        'AAT': 'N', 'AAC': 'N', 'CAT': 'H', 'CAC': 'H', 'GAA': 'E',
                        'GAG': 'E', 'GAT': 'C', 'GAC': 'C', 'AAA': 'K', 'AAG': 'K',
                        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
                        'AGG': 'R', 'TAA': '*', 'TAG': '*', 'TGA': '*'}
    # Uppercase sequence and remove possible spaces
    dna_sequence = dna_sequence.upper().replace(" ", "")

    if search_for_startcodon:
        start = None                            # Translation start position
        for i in range(len(dna_sequence)-2):
            codon = dna_sequence[i:i+3]
            if codon == 'ATG':
                start = i
                break
        if start is None:
            print("No start codon found for the sequence. Translates from the start.")
            start = 0
    else:
        start = 0
        
    pos = start                                 # Start translating at this position
    aa = ""
    aa_sequence = ""                            # Store amino acid sequence
    while pos < len(dna_sequence)-2 and aa != "*":
        codon = dna_sequence[pos:pos+3]         # Extract codon
        try:
            aa = amino_acid_table[codon]        # Translate to amino acid
        except KeyError as err:
            print("Undefined DNA codon found in sequence:", err)
            sys.exit(1)
        aa_sequence += aa
        pos += 3                                # Stepsize 3 to walk over codons

    if aa_sequence[-1] != "*":
        print("DNA sequence didn't end with a stopcodon.")
    else:
        aa_sequence = aa_sequence[:-1]			# Remove stop "*" at the end		

    return aa_sequence

if __name__ == "__main__":    
    print(translate_dna_to_aa("AGCAGAAAAGTAATGAACAAAGTGATAACCTAATAA"))