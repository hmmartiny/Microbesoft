#!/usr/bin/env python3
# coding=utf-8
import argparse
import os
import subprocess
import consensus

def get_args():
    
    parser = argparse.ArgumentParser(description="Align a fasta file")
    parser.add_argument("-in", "--infile", required=True)
    parser.add_argument("-out", "--outfile", help='Outfile name. Default is infile with "align" added.')
    
    args = parser.parse_args()
    if not args.outfile:
        args.outfile = add_ending(args.infile, "align")
    
    return args


def add_ending(fname, ending):
    root, extension = os.path.splitext(fname)
    return root + "_" + ending + extension


def yield_fasta(fname):
    with open(fname, 'r') as infile:
        header = ''
        sequence = ''
        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                if header and sequence:
                    yield header, sequence
                header = line.lstrip('>')
                sequence = ''
            else:
                sequence += line
        yield header, sequence


def read_fasta(fname):
    return list(zip(*yield_fasta(fname)))


def get_n_sequences(fname):
    return sum(1 for header, sequence in yield_fasta(fname))


def align(infile, outfile, timeout):
    command = "mafft %s > %s" % (infile, outfile)

    process = subprocess.Popen(command, shell=True)
    try:
        # wait for job to end
        process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        print("Subprocess timed out. Retrying file:", args.infile)
        align(infile, outfile, timeout)


def main(args):
    
    n_sequences = get_n_sequences(args.infile)
    print("Number of sequences:", n_sequences)
    
    align(args.infile, args.outfile, n_sequences * 10)
    
    headers, sequences = read_fasta(args.outfile)
    consensus_sequence, consensus_frequencies = consensus.consensus(sequences)
    
    


if __name__ == '__main__':
    args = get_args()
    main(args)
    print("# Done!")


