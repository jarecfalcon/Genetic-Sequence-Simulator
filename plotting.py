# ======================
# File: plotting.py
# ======================
"""Simple plotting utilities for DNA sequence analyses."""

import matplotlib.pyplot as plt


def plot_nucleotide_distribution(counts):
    """Display a bar chart of nucleotide counts.

    Args:
        counts (dict): Mapping of nucleotide to count.
    """
    labels = list(counts.keys())
    values = [counts[n] for n in labels]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
    plt.title("Nucleotide Composition")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
