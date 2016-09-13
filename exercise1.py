# Exercise 1.1a
    # ls -F
    # ls -F
    # ls -G
    # ls -l
    # ls -lh
    # ls -lS
    # ls -FGLh
    # ls -a gives all the files in folders with .files
# Exercise 1.1b
    # -i should be used when using -rf to be sure before deletion
# Exercise 1.1c
    # ls / gives the folders and files in the root of the machine
# Exercise 1.2
    # worked by copy everything from jb_bashrc in misc folder of bootcamp

# Exercise 1.3a
def reverse_complement(seq):
    """Compute reverse complement of a sequence."""
    # Initialize reverse complement
    rev_comp = ''

    for base in seq[::-1]:
        if base in 'Aa':
            rev_comp +='T'
        elif base in 'Tt':
            rev_comp += 'A'
        elif base in 'Gg':
            rev_comp += 'C'
        else:
            rev_comp += 'G'
    print(rev_comp)

#rev_seq = seq.lower()
#rev_seq = rev_seq.replace('t', 'A')
#rev_seq = rev_seq.replace('a', 'T')
#rev_seq = rev_seq.replace('g', 'C')
#rev_seq = rev_seq.replace('c', 'G')
#print()
# Exercise 1.3b
def reverse_complement2(seq):
    """Compute reverse complement of a sequence."""

    seq = seq[::-1].upper()
    seq = seq.replace('A','t')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    print(seq.upper())


# Exercise 1.4
str1 = 'ATCGGTCATCGATTA'
str2 = 'CTAGTAAATCGAT'


def longest_common_str(str1, str2):
    """determining the longest common substring."""
    common = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i: i+j] in str2:
                common.append(str1[i: i+j])
    print(max(common, key = len))


# Exercise 1.5a
def RNA_hairpin(seq):
    """determining the RNA secondary hairpins."""
    if seq.count('(') == seq.count(')') and seq.count('...') >= 1:
        print('True')
    else:
        print('False')


def parens_count(struc):
"""Ensure there are equal number of open and closed parentheses in the structure."""
    return struc.count('(') == struc.count(')')
    print(parens_count('....'))


# Exercise 1.5b
def dot_parens_to_bp(seq):
    """
    Convert a dot-parens structure to a list os base pairs.
    Return False if the structure is invalid.
    """
    if not parens_count(struc):
        print('Error in input structure.')
        return False
    # Initialize list of open parens and list of base pairs
    open_parens = []
    bps = []

    # Scan through substring
    for i, x in enumerate(struc):
        if x == '(':
            open_parens.append(i)
        elif x == ')':
            if len(open_parens) > 0
                bps.append((open_parens.pop(), i))
            else:
                print('Error in input structure.')
                return False
    # Return the result as a tuple
    return tuple(sorted(bps))


# Exercise 1.5c
def hairpin_check(bps):
    """Check to make sure no hairpins are too short."""
    for bp in bps:
        if bp[1] - bp [0] < 4:
            print('A hairpin is too short.')
            return False

    # Everything checks out
    return True


# Exercise 1.5d
def rna_ss_validator(seq, sec_struc, wobble=True):
    """Validate and RNA structure."""
    # Convert structure to base pairs
    bps = dot_parens_to_bp(sec_struc)

    # If this failed, the structure is invalid
    if not bps:
        return False

    # Do the hairpin check
    if not hairpin_check(bps):
        return False

    # Possible base pairs
    if wobble:
        ok_bps = ('gc', 'cg', 'au', 'ua', 'gu', 'ug')
    else:
        ok_bps = ('gc', 'cg', 'au', 'ua')

    # Check complementarity
    for bp in bps:
        bp_str = (seq[bp[0]]) + seq[bp[1]]).lower()
        if bp_str not in ok_bps:
            print('Invalid base pair.')
            return False

    # Everything passed
    return True
