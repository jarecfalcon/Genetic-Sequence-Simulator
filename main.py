# =======================
# File: main.py
# =======================

from input_module import get_sequence, load_sequence_from_file
from analysis_module import (
    count_nucleotides,
    sequence_length,
    gc_content,
    transcribe,
    get_complement,
    reverse_complement
)  
from utils import clear_screen, print_header

def main():
    print_header("DNA Sequence Analysis Tool")
    
    # Get sequence from user or file
    choice = input("Do you want to enter a sequence (E) or load from file (F)? ").strip().upper()
    if choice == 'E':
        sequence = get_sequence()
    elif choice == 'F':
        file_path = input("Enter the path to the DNA sequence file: ").strip()
        sequence = load_sequence_from_file(file_path)
    else:
        print("Invalid choice. Exiting.")
        return
    
    # Perform analysis
    print_header("Analysis Results")
    print(f"Sequence: {sequence}")
    print(f"Length: {sequence_length(sequence)}")
    print(f"GC Content: {gc_content(sequence):.2f}%")
    print(f"Nucleotide Counts: {count_nucleotides(sequence)}")
    print(f"Transcribed RNA: {transcribe(sequence)}")
    print(f"Complement: {get_complement(sequence)}")        

    print(f"Reverse Complement: {reverse_complement(sequence)}")
    print("\nAnalysis complete.")   

if __name__ == "__main__":
    main()