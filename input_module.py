#======================
# File: input_module.py
#======================


def get_sequence():
    """Get a DNA sequence from user input."""
    seq = input("Enter a DNA sequence (A, T, C, G only): ").strip().upper()
    if all(ch in {"A", "T", "C", "G"} for ch in seq) and seq:
        return seq
    raise ValueError("Invalid DNA sequence. Please enter a valid sequence containing A, T, C, G only.")


def load_sequence_from_file(file_path):
    """Load a DNA sequence from a file."""
    try:
        with open(file_path, "r") as file:
            seq = file.read().strip().upper()
            if all(ch in {"A", "T", "C", "G"} for ch in seq) and seq:
                return seq
            raise ValueError("Invalid DNA sequence in file.")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {file_path}") from exc
