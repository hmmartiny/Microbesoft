#!/usr/bin/env python3
# coding=utf-8

import argparse
import os
import subprocess
import numpy as np

AA_alphabet = "ARNDCEQGHILKMFPSTYWV"
AA_alphabet_gap = AA_alphabet + '-' + 'X'

def consensus(sequences):
    """Get consensus sequence and conservation rate."""
    n_sequences = len(sequences)
    sequences = [np.asarray(list(sequence.upper())) for sequence in sequences]
    sequence_matrix = np.vstack(sequences)
    
    # fill a matrix with the frequencies for each amino acid in the alphabet
    frequency_matrix = np.zeros((len(AA_alphabet_gap), sequence_matrix.shape[1]))
    for i, amino_acid in enumerate(AA_alphabet_gap):
        indexes = amino_acid == sequence_matrix
        frequency_matrix[i,:] = np.sum(indexes, axis=0)
    # from sums to fractions
    frequency_matrix /= n_sequences
    
    consensus_amino_acids_index = np.argmax(frequency_matrix, axis=0)
    consensus_amino_acids = [AA_alphabet_gap[index] for index in consensus_amino_acids_index]
    # to string
    consensus_amino_facids = ''.join(consensus_amino_acids)
    consensus_amino_acid_frequencies = []
    for i in range(n_sequences):
        consensus_amino_acid_frequencies.append(frequency_matrix[consensus_amino_acids_index[i], i])

    return consensus_amino_acids, consensus_amino_acid_frequencies


def findConsensus(sequences):
    n_sequences = len(sequences)            # number of sequences
    n_length = len(list(sequences)[0])      # sequence length

    # convert sequences to giant matrix
    sequences = [np.asarray(list(sequence.upper())) for sequence in sequences]
    sequence_matrix = np.vstack(sequences)

    # get aa frequences at each position
    frequency_matrix = np.empty((n_length, len(AA_alphabet_gap)))
    for i, amino_acid in enumerate(AA_alphabet_gap):
        idxs = np.sum(amino_acid == sequence_matrix, axis=0)
        frequency_matrix[:, i] = idxs

    # find the highest frequency at each position
    consensus_aa_freqs = np.argmax(frequency_matrix, axis=1)

    consensus_amino_acids = [AA_alphabet_gap[index] for index in consensus_aa_freqs]

    return consensus_amino_acids, consensus_aa_freqs
