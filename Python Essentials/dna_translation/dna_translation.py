codon_table = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',

    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',

    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',

    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

amino_acid_table = {
    'A': "alanine",
    'C': "cystine",
    'D': "aspartic acid",
    'E': "glutamic acid",
    'F': "phenylalanine",
    'G': "glycine",
    'H': "histidine",
    'I': "isoleucine",
    'K': "lysine",
    'L': "leucine",
    'M': "methionine/start",
    'N': "asparagine",
    'P': "proline",
    'Q': "glutamine",
    'R': "arginine",
    'S': "serine",
    'T': "threonine",
    'V': "valine",
    'W': "tryptophan",
    'Y': "tyrosine",
    '*': "stop",
}

sequence = (
    "AACCTGCTCTTTAGATTTCGAGCTTATTCTCTTCTAGCAGTTTCTTGCCACCATGTCGGAAACCGCTCCT" +
    "GCCGAGACAGCCACCCCAGCGCCGGTGGAGAAATCCCCGGCTAAGAAGAAGGCAACTAAGAAGGCTGCCG" +
    "GCGCCGGCGCTGCTAAGCGCAAAGCGACGGGGCCCCCAGTCTCAGAGCTGATCACCAAGGCTGTGGCTGC" +
    "TTCTAAGGAGCGCAATGGCCTTTCTTTGGCAGCCCTTAAGAAGGCCTTAGCGGCCGGTGGCTACGACGTG" +
    "GAGAAGAATAACAGCCGCATTAAGCTGGGCCTCAAGAGCTTGGTGAGCAAGGGCACCCTGGTGCAGACCA" +
    "AGGGCACTGGTGCTTCTGGCTCCTTTAAACTCAACAAGAAGGCGGCCTCCGGGGAAGCCAAGCCCAAAGC" +
    "CAAGAAGGCAGGCGCCGCTAAAGCTAAGAAGCCCGCGGGGGCCACGCCTAAGAAGGCCAAGAAGGCTGCA" +
    "GGGGCGAAAAAGGCAGTGAAGAAGACTCCGAAGAAGGCGAAGAAGCCCGCGGCGGCTGGCGTCAAAAAGG" +
    "TGGCGAAGAGCCCTAAGAAGGCCAAGGCCGCTGCCAAACCGAAAAAGGCAACCAAGAGTCCTGCCAAGCC" +
    "CAAGGCAGTTAAGCCGAAGGCGGCAAAGCCCAAAGCCGCTAAGCCCAAAGCAGCAAAACCTAAAGCTGCA" +
    "AAGGCCAAGAAGGCGGCTGCCAAAAAGAAGTAGGAAGCTGGCGTGTGAAAACCGCAACAAAGCCCCAAAG" +
    "GCTCTTTTCAGAGCCACCCA"
)

loc = sequence.find('ATG')
amino_acids = ""

while True:
    codon = sequence[loc:loc + 3]
    amino_acid = codon_table[codon]
    if amino_acid == '*':
        break
    amino_acids += amino_acid
    loc += 3
    
print amino_acids

print "The number of amino acids is", len(amino_acids)

for code, amino_acid in amino_acid_table.items():
    if code in amino_acids:
        print amino_acid + " is in protein"
    else:
        print amino_acid + " is not in protein"
        
#BONUS
#TODO: UNDERSTANT BONUS QUESTION