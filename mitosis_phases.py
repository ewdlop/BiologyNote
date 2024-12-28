def mitosis_phases():
    """Simulate the phases of mitosis."""
    phases = [
        "Interphase: Cell prepares for division (DNA replication, growth).",
        "Prophase: Chromosomes condense, spindle fibers form.",
        "Metaphase: Chromosomes align at the equator.",
        "Anaphase: Sister chromatids separate and move to opposite poles.",
        "Telophase & Cytokinesis: Chromosomes de-condense, cytoplasm divides."
    ]

    print("Phases of Mitosis:")
    for i, phase in enumerate(phases, 1):
        print(f"Phase {i}: {phase}")

    return "Cell division complete: Two identical daughter cells formed."

# Example
mitosis_result = mitosis_phases()
print("\nResult:", mitosis_result)
