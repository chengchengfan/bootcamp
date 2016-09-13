"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """
    Convert a DNA sequence to RNA/
    """

    # Convert to uppercase
    seq = seq.lower()

    return seq.replace('t', 'u')
