"""
DNA Translation
---------------

If you haven't done the "DNA String" or the "DNA Dictionary" exercises then you
probably should do those exercises before attempting this one.

Sequences of DNA are frequently represented by strings of letters corresponding
to the bases:

    "A" is adenine
    "C" is cytosine
    "G" is guanine
    "T" is thymine

A gene encodes a protein by specifying the amino acids that compose it via
groups of 3 bases (called "codons").  Each codon corresponds to an amino acid
or a special "start" or "stop" sequence.

In the usual genetic code the sequence "ATG" indicates the start of the
encoding of the protein (and also encodes the amino acid methionine).  The
three codons "TAA", "TAG" and "TGA" are stop codons and indicate that the
protein is finished.

In the code below there is a dictionary ``codon_table`` that maps codons to
their corresponding amino acid abbreviations

In this example, we will look at a genetic sequence from the human genome which
encodes the `histone cluster 1, H1b.`_

::

      A ACC TGC TCT TTA GAT TTC GAG CTT ATT CTC TTC TAG CAG TTT CTT GCC
    ACC ATG TCG GAA ACC GCT CCT GCC GAG ACA GCC ACC CCA GCG CCG GTG GAG
    AAA TCC CCG GCT AAG AAG AAG GCA ACT AAG AAG GCT GCC GGC GCC GGC GCT
    GCT AAG CGC AAA GCG ACG GGG CCC CCA GTC TCA GAG CTG ATC ACC AAG GCT
    GTG GCT GCT TCT AAG GAG CGC AAT GGC CTT TCT TTG GCA GCC CTT AAG AAG
    GCC TTA GCG GCC GGT GGC TAC GAC GTG GAG AAG AAT AAC AGC CGC ATT AAG
    CTG GGC CTC AAG AGC TTG GTG AGC AAG GGC ACC CTG GTG CAG ACC AAG GGC
    ACT GGT GCT TCT GGC TCC TTT AAA CTC AAC AAG AAG GCG GCC TCC GGG GAA
    GCC AAG CCC AAA GCC AAG AAG GCA GGC GCC GCT AAA GCT AAG AAG CCC GCG
    GGG GCC ACG CCT AAG AAG GCC AAG AAG GCT GCA GGG GCG AAA AAG GCA GTG
    AAG AAG ACT CCG AAG AAG GCG AAG AAG CCC GCG GCG GCT GGC GTC AAA AAG
    GTG GCG AAG AGC CCT AAG AAG GCC AAG GCC GCT GCC AAA CCG AAA AAG GCA
    ACC AAG AGT CCT GCC AAG CCC AAG GCA GTT AAG CCG AAG GCG GCA AAG CCC
    AAA GCC GCT AAG CCC AAA GCA GCA AAA CCT AAA GCT GCA AAG GCC AAG AAG
    GCG GCT GCC AAA AAG AAG TAG GAA GCT GGC GTG TGA AAA CCG CAA CAA AGC
    CCC AAA GGC TCT TTT CAG AGC CAC CCA

1) Write Python code that:

   a. Finds the first start codon in the sequence (Hint: remember what you did
      in the "DNA String" exercise).

   b. Loops over the codons, building a string of the abbreviations of the
      protein's amino acids (eg. the protein should start with "MSETAPA...")

   c. Stops when it reaches a stop codon.

   d. Prints out the amino acid string.

2) Print the number of amino acids in the protein.

3) There is another dictionary ``amino_acid_table`` that maps the
   abbreviations to their full names.  Take the string of the abbreviations of
   the amino acids and print  out for each amino acid its full name and
   whether or not it is used by the protein.

Bonus
-----

4) Because most amino acids have multiple codons which can produce them, there
   are many different sequences that will potentially produce this protein.
   Compute how many there are.

Note
----

If you need to do this sort of bioinformatics manipulation, the "Biopython"
library does all of these sorts of things and more.

References
----------

_ http://www.ncbi.nlm.nih.gov/nuccore/NM_005322

"""

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

# 1) a. Find the location first start codon.

location = sequence.find('ATG')

# 1) b. and c. Loop, building a string of abbreviations for amino acids

amino_acids = ""

# your code goes here
while True:
    codon = sequence[location:location + 3]
    amino_acid = codon_table[codon]
    if amino_acid == '*':
        break
    amino_acids += amino_acid
    location += 3

# 1) d. Print out the string

print amino_acids

# 2) Print the number of amino acids in the protein

print "The number of amino acids is", len(amino_acids)

# 3) For each amino acid, print its name and whether or not it is in the
#    protein.

for code, amino_acid in amino_acid_table.items():
    if code in amino_acids:
        print amino_acid + " is in protein"
    else:
        print amino_acid + " is not in protein"

# Bonus
# 4) How many different sequences could produce this protein?

# build a table of amino acid -> number of codons
codon_count = {code: 0 for code in amino_acid_table}
for codon, amino_acid in codon_table.items():
    codon_count[amino_acid] += 1

# now for each amino acid, multiply together the choices
combinations = 1
for amino_acid in amino_acids:
    combinations *= codon_count[amino_acid]

# aren't you glad Python handles arbitrarily long integer values :)
print "There are {0} different ways of encoding this protein".format(combinations)
