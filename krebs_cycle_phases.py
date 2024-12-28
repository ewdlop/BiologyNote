def krebs_cycle_phases(pyruvate):
    """Simulate the phases of the Krebs Cycle for a given pyruvate count."""
    phases = [
        "Condensation: Acetyl-CoA + Oxaloacetate → Citrate",
        "Isomerization: Citrate → Isocitrate",
        "Decarboxylation 1: Isocitrate → α-Ketoglutarate + NADH",
        "Decarboxylation 2: α-Ketoglutarate → Succinyl-CoA + NADH",
        "Substrate-Level Phosphorylation: Succinyl-CoA → Succinate + ATP",
        "Oxidation 1: Succinate → Fumarate + FADH₂",
        "Hydration: Fumarate → Malate",
        "Oxidation 2: Malate → Oxaloacetate + NADH"
    ]

    outputs = {
        "ATP": pyruvate * 1,
        "NADH": pyruvate * 4,
        "FADH2": pyruvate * 1
    }

    print(f"Krebs Cycle Phases for {pyruvate} pyruvate(s):")
    for i, phase in enumerate(phases, 1):
        print(f"Phase {i}: {phase}")
    
    return outputs

# Example
pyruvate_count = 2
krebs_output = krebs_cycle_phases(pyruvate_count)
print("\nFinal Outputs:", krebs_output)
