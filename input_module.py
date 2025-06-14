#======================
# File: input_module.py
#======================

def get_sequence():
    """
    Get a DNA sequence from user input.
    
    Returns:
        str: The DNA sequence entered by the user.
    """
    seq = input("Enter a DNA sequence (A, T, C, G only): ").strip().upper()
    if all(ch in {"A", "T", "C", "G"} for ch in seq) and seq:
        return seq
    else:
        raise ValueError("Invalid DNA sequence. Please enter a valid sequence containing A, T, C, G only.")




def load_sequence_from_file(file_path):
    """
    Load a DNA sequence from a file.
    
    Args:
        file_path (str): The path to the file containing the DNA sequence.
        
    Returns:
        str: The DNA sequence read from the file.
    """
    try:
        with open(file_path, 'r') as file:
            seq = file.read().strip().upper()
            if all(ch in {"A", "T", "C", "G"} for ch in seq) and seq:
                return seq
            else:
                raise ValueError("Invalid DNA sequence in file.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise e
    
    