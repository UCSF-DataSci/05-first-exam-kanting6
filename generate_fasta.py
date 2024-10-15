import random
import os
import textwrap

# Use function to generate a random DNA sequence
def generate_random_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

# Use fnction to save the DNA sequence in FASTA format
def save_fasta(sequence, filename):
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Create the path for the file
    filepath = os.path.join('data', filename)

    # Write the sequence to the file in FASTA format
    with open(filepath, 'w') as fasta_file:
        fasta_file.write(">random_sequence\n")  # FASTA header
        # Use textwrap to format the sequence into 80-character lines
        fasta_file.write('\n'.join(textwrap.wrap(sequence, 80)))

# Main function
def main():
    sequence_length = 1_000_000  # 1 million base pairs
    random_dna_sequence = generate_random_dna_sequence(sequence_length)
    save_fasta(random_dna_sequence, 'random_sequence.fasta')
    print(f"Random DNA sequence saved in data/random_sequence.fasta")

if __name__ == "__main__":
    main()

