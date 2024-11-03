#Yuanbo Pang


codon_table = {
    'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
    'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
    'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met',
    'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
    'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
    'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': '***', 'TAG': '***',
    'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'TGT': 'Cys', 'TGC': 'Cys', 'TGA': '***', 'TGG': 'Trp',
    'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}


def clean_sequence(sequence):

    result = ''
    for char in sequence:
        if char.isalpha():
            result += char.upper()
    return result


def process_sequence(sequence):

    cleaned_seq = clean_sequence(sequence)
    if len(cleaned_seq) % 3 != 0:
        print("Error: You must give complete triples.\n")
        return
    index = 0
    while index < len(cleaned_seq):
        codon = cleaned_seq[index:index + 3]
        if set(codon) - {'A', 'C', 'G', 'T'}:
            print(f"{codon} invalid sequence")
        else:
            amino_acid = codon_table.get(codon, 'Invalid')
            if amino_acid == 'Invalid':
                print(f"{codon} invalid sequence")
            else:
                print(f"{codon} {amino_acid}")
        index += 3
    print()


def main():
    while True:
        user_input = input("Enter a nucleotide sequence, or just press ENTER to quit: ")
        if not user_input.strip():
            break
        process_sequence(user_input)


if __name__ == "__main__":
    main()
