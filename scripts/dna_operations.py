import argparse

# Function to return the complement of a DNA sequence
def complement(sequence):
    complement_dict = str.maketrans('ACGTacgt', 'TGCAtgca')
    return sequence.translate(complement_dict)

# Function to return the reverse of a DNA sequence
def reverse(sequence):
    return sequence[::-1]

# Function to return the reverse complement of a DNA sequence
def reverse_complement(sequence):
    return reverse(complement(sequence))

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Process a DNA sequence.')
    parser.add_argument('sequence', type=str, help='The DNA sequence to process.')
    args = parser.parse_args()

    sequence = args.sequence

    # Output the results
    print("Original sequence:        ", sequence)
    print("Complement:               ", complement(sequence))
    print("Reverse:                  ", reverse(sequence))
    print("Reverse complement:       ", reverse_complement(sequence))

if __name__ == "__main__":
    main()


