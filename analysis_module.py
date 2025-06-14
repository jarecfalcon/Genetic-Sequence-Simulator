#=========================
# File: analysis_module.py
#=========================

from collections import Counter


def count_nucleotides(sequence):
    """Return a dictionary with the count of each nucleotide in the sequence."""
    return Counter(sequence)


def sequence_length(sequence):
    """Return the length of the DNA sequence."""
    return len(sequence)


def gc_content(sequence):
    """Calculate the GC content of the DNA sequence as a percentage."""
    if not sequence:
        return 0.0
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100


def transcribe(sequence):
    """Transcribe a DNA sequence to RNA by replacing 'T' with 'U'."""
    return sequence.replace('T', 'U')


def get_complement(sequence):
    """Return the complementary DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in sequence)


def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    return get_complement(sequence)[::-1]
