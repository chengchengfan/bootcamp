# Exercise 2.1 - done at terminal

# Exercise 2.2a

# Exercise 2.3a
def gc_blocks(seq, block_size):
    """Dividing a sequence into blocks and to compute GC content."""

    # Making empty lsit for tuple for GC content
    gc_content = []

    # Defining block
    block = []

    # Defining first i
    i = 0

    # Making blocks
    for i in range(0,len(seq), block_size):
        print(i)
        block.append(seq[i:i+ block_size])

    # Making everything uppercase
    seq = seq.upper()

    # Initialize GC counter
    for subseq in block:
        gc_count = subseq.count('G') + subseq.count('C')
        gc_content.append(gc_count / block_size)

    return gc_content

# Exercise 2.3b
def gc_map(seq, block_size, gc_thresh):
    """Returning GC content above threshold is capitalized
    and every base in a block below the threshold is lowercase."""
    # Making empty lsit for tuple for GC content
    gc_content = []
    # Defining block
    blocks = []
    # Defining first i
    i = 0
    # Making blocks
    for i in range(0,len(seq), block_size):
        print(i)
        blocks.append(seq[i:i+ block_size])
        # Making everything lowercase
        seq = seq.lower()
        # Initialize GC counter
        for block in blocks:
            for subseq in block:
                block_gc_count = subseq.count('g') + subseq.count('c')
                block_gc_content = block_gc_count / block_size
                # Defining threshold
                if block_gc_content[i] > gc_thresh:
                    print(block[i].upper())
                elif block_gc_content[i] < gc_thresh:
                    print(block[i])
        print(blocks)

    return ''.join(blocks)
