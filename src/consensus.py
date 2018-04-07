#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import subprocess
import numpy as np

amino_acid_alphabet = "ARNDCEQGHILKMFPSTYWV"

def consensus(sequences):
    """Get consensus sequence and conservation rate."""
    n_sequences = len(sequences)
    sequences = [np.asarray(list(sequence)) for sequence in sequences]
    sequence_matrix = np.vstack(sequences)
    
    # fill a matrix with the frequencies for each amino acid in the alphabet
    frequency_matrix = np.zeros((len(amino_acid_alphabet), sequence_matrix.shape[1]))
    for i, amin_acid in enumerate(amino_acid_alphabet):
        indexes = amin_acid == sequence_matrix
        frequency_matrix[i,:] = np.sum(indexes, axis=0)
    # from sums to fractions
    frequency_matrix /= n_sequences
    
    consensus_amino_acids_index = np.argmax(frequency_matrix, axis=0)
    consensus_amino_acids = [amino_acid_alphabet[index] for index in consensus_amino_acids_index]
    # to string
    consensus_amino_acids = ''.join(consensus_amino_acids)
    consensus_amino_acid_frequencies = []
    for i in range(n_sequences):
        consensus_amino_acid_frequencies.append(frequency_matrix[consensus_amino_acids_index[i], i])
    
    return consensus_amino_acids, consensus_amino_acid_frequencies

