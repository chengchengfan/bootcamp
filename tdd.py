import pytest
import bioinfo_dicts

def n_neg(seq):
    """ Number of negative residues in a protein sequence."""

    # Convert to all upper case
    seq = seq.upper()

    # Check the valiality of sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')
    # Count E and D and return Count
    return seq.count('D') + seq.count('E')
