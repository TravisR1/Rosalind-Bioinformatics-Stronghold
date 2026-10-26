#Counting DNA Nucleotides
#Given a DNA string, return the count of each nucleotide (A, C, G, T) in the string.
#Output should be in the order of A, C, G, T separated by spaces.

def count_nucleotides(dna_string):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for nucleotide in dna_string:
        if nucleotide in counts:
            counts[nucleotide] += 1

    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

dna_string = "dna_string.txt"

with open(dna_string, 'r') as file:
    dna_sequence = file.read().strip()
    print(count_nucleotides(dna_sequence))