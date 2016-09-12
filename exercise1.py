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


def longest_common_str(seq):
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


# Exercise 1.5b
def dotparen_to_bp(seq):
    """a tuple of 2-tuples representing the base pairs."""
    pairs = ()
    for i in range(len(seq)):
        one = seq[i]
        two = reversed(seq[i])
        pairs.append((one, two))
    print(pairs)
