'''
notes:
    - mutation: mistale that occurs during copying/creation of a nucleic acid, esp DNA
    - point mutation: replaces one base with another at a single nucelotide
        - Hamming distance: minimum number of point mutations that occurred during evolution betweeen the two strands
            - the diff between two homologous DNA strands from diff genomes with a common ancestor
            - only defined for seqs of equal length
            - if unequal length, compute hamming distance over the shorter length

input: make a DNA class that passes the tests

rules:
    - make a DNA class
        - iv's: 
            - stand is a string
        - methods:
            - hamming_distance(string_of_other_strand)
                - if one is longer, only compare up to the length of that strand. the additional bases are simply ignored and not counted as mutations


DS:
    - strings

Alg:
    - 

'''
class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, other):
        count = 0

        if len(self.strand) <= len(other):
            shorter = self.strand
            longer = other
        else:
            shorter = other
            longer = self.strand
        
        for idx, char in enumerate(shorter):
            if char != longer[idx]:
                count += 1

        return count

