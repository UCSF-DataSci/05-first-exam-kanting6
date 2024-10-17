import sys
import os

def find_cutsites(fasta_file, cut_site):
    # Remove the '|' character from the cut site sequence
    cut_site = cut_site.replace('|', '')

    # Read the DNA sequence from the FASTA file
    with open(fasta_file, 'r') as f:
        dna_sequence = f.read().replace('\n', '')  # Remove all newlines
    
    # Find all occurrences of the cut site in the DNA sequence
    cut_positions = []
    start = 0
    while True:
        start = dna_sequence.find(cut_site, start)
        if start == -1:
            break
        cut_positions.append(start)
        start += len(cut_site)  # Move past the current cut site
        
    print(f"Total cut sites found: {len(cut_positions)}\n")

    # Find pairs of cut sites that are 80,000 - 120,000 bp apart
    cut_pairs = []
    for i in range(len(cut_positions)):
        for j in range(i + 1, len(cut_positions)):
            distance = cut_positions[j] - cut_positions[i]
            if 80000 <= distance <= 120000:
                cut_pairs.append((cut_positions[i], cut_positions[j]))

    # Print results
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_pairs)}")
    for i, pair in enumerate(cut_pairs[:5]):
        print(f"Pair {i + 1}: {pair}")

    # Save the results to a file
    os.makedirs('results', exist_ok=True)
    with open('results/distant_cutsite_summary.txt', 'w') as summary_file:
        summary_file.write(f"Total number of cut site pairs: {len(cut_pairs)}\n")
        for i, pair in enumerate(cut_pairs[:5]):
            summary_file.write(f"Pair {i + 1}: {pair}\n")


if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <FASTA_file_path> <cut_site_sequence>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]

    # Call the function with the provided arguments
    find_cutsites(fasta_file, cut_site)
