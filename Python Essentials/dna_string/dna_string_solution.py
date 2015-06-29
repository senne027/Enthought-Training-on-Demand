"""
DNA String
----------

Sequences of DNA and RNA are frequently represented by strings of letters
corresponding to the bases:

    "A" is adenine
    "C" is cytosine
    "G" is guanine
    "T" is thymine
    "U" is uracil which replaces thymine in RNA

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


1)  In bioinformatics it is common to store the "coding" strand of DNA.  When
    a gene is expressed, the first thing that happens is that a copy is made
    of the sequence in messenger RNA (mRNA).  This sequence of mRNA is the
    same as the sequence of coding DNA, except that the thymine bases have
    been replaced by uracil bases.

    Compute the equivalent mRNA sequence to the sequence in this example.

    Hint: see if there is a string method that lets you _replace_ substrings.

2)  The other half of a DNA molecule is the "template" strand of the DNA.
    This strand holds the other half of each base pair, so that:

    * adenine "A" is replaced by thymine "T"
    * thymine "T" is replaced by adenine "A"
    * cytosine "C" is replaced by guanine "G"
    * guanine "G" is replaced by cytosine "C"

    In addition, convention holds that the sequence is written in the reverse
    order.

    Compute the template DNA sequence which corresponds to the provided
    sequence.

    Hint: Look at the documentation for the `translate` method on strings and
    the `maketrans` function from the `string` module (which we have imported
    for you).

    Hint 2: remember the how to use slicing to reverse a string

    Question: why can't you use the same method you used in (1)?

3)  A gene encodes a protein by specifying the amino acids that compose it via
    groups of 3 bases (called "codons").  In the usual genetic code the
    sequence "ATG" indicates the start of the encoding of the protein.

    Find the index of the start of the coding section of the sequence.

    Hint: look for a string method that helps you _find_ a substring.

4)  The end of the encoding of a protein is indicated by one of three "stop"
    codons: "TAA", "TAG" or "TGA".  In this case the stop is 'TAG'.  Find the
    'TAG' codon closest to the end of the sequence.

    Hint: look for a string method that helps you find from the _right_ of
    a string.

Note
----

If you need to do this sort of bioinformatics manipulation, the "Biopython"
library does all of these sorts of things and more.


References
----------

_ http://www.ncbi.nlm.nih.gov/nuccore/NM_005322

"""

from string import maketrans

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

# 1) translate the genetic sequence to mRNA by replacing thymine with uracil.

mrna_sequence = sequence.replace('T', 'U')

print mrna_sequence

# 2) translate the genetic sequence to template DNA by replacing:
#      adenine "A" with thymine "T"
#      thymine "T" with adenine "A"
#      cytosine "C" with guanine "G"
#      guanine "G" with cytosine "C"
#    and reversing the string

coding_to_template = maketrans('ATCG', 'TAGC')

template_sequence = sequence.translate(coding_to_template)[::-1]

print template_sequence

# 3) find the first occurrence of 'ATG' in the sequence

start_index = sequence.find('ATG')

print "Start index:", start_index

# 4) find the last occurrence of 'TAG' in the sequence

end_index = sequence.rfind('TAG')

print "End index:", end_index
