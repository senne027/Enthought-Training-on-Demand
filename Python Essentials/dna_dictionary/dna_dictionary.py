
# DNA Dictionary
# ==============
# 
# If you haven't done the "DNA String" exercise in the lecture called "Introduction to Strings" then you probably should do that exercise before attempting this one.
# 
# Background
# ----------
# Sequences of DNA are frequently represented by strings of letters, each corresponding to a base:
# 
#     "A" is adenine
#     "C" is cytosine
#     "G" is guanine
#     "T" is thymine
# 
# A gene encodes a protein by specifying the amino acids that compose it via groups of 3 bases (called "codons").  Each codon corresponds to an amino acid or a special "start" or "stop" sequence.
# 
# In the usual genetic code the sequence "ATG" indicates the start of the encoding of the protein (and also encodes the amino acid methionine).  The three codons "TAA", "TAG" and "TGA" are stop codons and indicate that the protein is finished.
# 
# Question 1
# ----------
# 
# Below is a dictionary called ``codon_table`` that maps codons to their corresponding amino acid abbreviations (the stop codons are usually abbreviated by a `*`).  Extract the abbreviation associated with the codon "AAG".


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



# your code goes here


# Question 2
# ----------
# 
# We have created another dictionary ``amino_acid_table`` that maps the amino acid abbreviations to their full names.  Extract the full name of the amino acid associated with the codon "CAA".


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



# your code goes here


# Question 3
# ----------
# 
# Human mitochondrial DNA has a slightly different genetic code where "AGA" and "AGG" are additional "stop" codons, "TGA" is not a "stop" codon but instead codes for tryptophan, and "ATA" codes for methionine instead of isoleucine.
# 
# Copy the codon table into a new `mitochondrial_table` and modify the dictionary so that it corresponds to the mitochondrial DNA genetic code.
# 
# Note: You don't need to manually copy the whole table in the editor. Instead see if you can find dictionary methods to copy the `codon_table`. We will review all dictionary methods at the next lecture, so this is a preview.

# Hint: Remember that to find methods (tools) attached to an object, create a notebook cell, create any dictionary inside and then type dot and then the TAB key. For example 
# <pre>
# {}.[HIT THE TAB KEY HERE]
# </pre>


# your code goes here


# Question 4 (Bonus)
# ------------------
# 
# If you already know about writing loops in Python, build programatically a list of all of the codons that can produce serine.
# 


# your code goes here


# Note
# ----
# 
# If you need to do this sort of bioinformatics manipulation, the ["Biopython" library](http://biopython.org/wiki/Main_Page) does all of these sorts of things like this and more. Check it out.
# 
