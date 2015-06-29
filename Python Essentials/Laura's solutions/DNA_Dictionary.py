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

codon = "AAG"

abbreviation = codon_table[codon]
print "AAG --> {0}".format(abbreviation)

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

codon = "CAA"

abb = codon_table[codon]
full_name = amino_acid_table[abb]
print "CAA -> {0}".format(full_name)

#Another way to do it:

print "CAA -> {0}".format(amino_acid_table[codon_table[codon]])

mitochondrial_table = codon_table.copy()

mitochondrial_table["AGA"] = '*'
mitochondrial_table["AGG"] = '*'
mitochondrial_table["TGA"] = 'W'
mitochondrial_table["ATA"] = 'M'

print mitochondrial_table

amino_acid = "serine"


codons = []
for codon, symbol in codon_table.items():
    if amino_acid_table[symbol] == amino_acid:
        codons.append(codon)

# It could be done using a list comprehension:
codons = [codon for codon, symbol in codon_table.items()
          if amino_acid_table[symbol] == amino_acid]

print "Codons that produce serine: {0}".format(codons)