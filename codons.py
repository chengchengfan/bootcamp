codon = input('Input your codon, please:')
codon_list = ['UAA', 'UAG', 'UGA']
codon_tuple = tuple(codon_list)
if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_list:
    print('This is the stop codon.')
else:
    print('This is neither a start nor stop codon.')
