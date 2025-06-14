# Test imports
from input_module import get_sequence, load_sequence_from_file

print("Testing input_module imports:")
try:
    seq = get_sequence()
    print(f"Input sequence: {seq}")
except Exception as exc:
    print(f"Error: {exc}")
