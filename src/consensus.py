#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import subprocess
import numpy as np

AA_alphabet = "ARNDCEQGHILKMFPSTYWV"
AA_alphabet_gap = AA_alphabet + '-'

def consensus(sequences):
    """Get consensus sequence and conservation rate."""
    n_sequences = len(sequences)
    sequences = [np.asarray(list(sequence.upper())) for sequence in sequences]
    sequence_matrix = np.vstack(sequences)
    
    # fill a matrix with the frequencies for each amino acid in the alphabet
    frequency_matrix = np.zeros((len(AA_alphabet_gap), sequence_matrix.shape[1]))
    for i, amin_acid in enumerate(AA_alphabet_gap):
        indexes = amin_acid == sequence_matrix
        frequency_matrix[i,:] = np.sum(indexes, axis=0)
    # from sums to fractions
    frequency_matrix /= n_sequences
    
    consensus_amino_acids_index = np.argmax(frequency_matrix, axis=0)
    consensus_amino_acids = [AA_alphabet_gap[index] for index in consensus_amino_acids_index]
    # to string
    consensus_amino_acids = ''.join(consensus_amino_acids)
    consensus_amino_acid_frequencies = []
    for i in range(n_sequences):
        consensus_amino_acid_frequencies.append(frequency_matrix[consensus_amino_acids_index[i], i])
    
    return consensus_amino_acids, consensus_amino_acid_frequencies



