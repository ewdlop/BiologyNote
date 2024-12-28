# Define constants for ATP production
ATP_GLYCOLYSIS = 2
ATP_KREBS_CYCLE = 2
ATP_ETC_PER_NADH = 3
ATP_ETC_PER_FADH2 = 2

# Initial quantities (per glucose molecule)
glucose = 1
pyruvate = 0
NADH = 0
FADH2 = 0
ATP = 0

# Glycolysis
def glycolysis(glucose):
    pyruvate_produced = glucose * 2
    NADH_produced = glucose * 2
    ATP_produced = ATP_GLYCOLYSIS
    return pyruvate_produced, NADH_produced, ATP_produced

# Krebs Cycle
def krebs_cycle(pyruvate):
    NADH_produced = pyruvate * 3
    FADH2_produced = pyruvate * 1
    ATP_produced = ATP_KREBS_CYCLE
    return NADH_produced, FADH2_produced, ATP_produced

# Electron Transport Chain
def electron_transport_chain(NADH, FADH2):
    ATP_from_NADH = NADH * ATP_ETC_PER_NADH
    ATP_from_FADH2 = FADH2 * ATP_ETC_PER_FADH2
    return ATP_from_NADH + ATP_from_FADH2

# Simulate Glycolysis
pyruvate, NADH_glycolysis, ATP_glycolysis = glycolysis(glucose)
ATP += ATP_glycolysis
NADH += NADH_glycolysis

print(f"After Glycolysis: Pyruvate={pyruvate}, NADH={NADH}, ATP={ATP}")

# Simulate Krebs Cycle (per pyruvate)
NADH_krebs, FADH2_krebs, ATP_krebs = krebs_cycle(pyruvate)
ATP += ATP_krebs
NADH += NADH_krebs
FADH2 += FADH2_krebs

print(f"After Krebs Cycle: NADH={NADH}, FADH2={FADH2}, ATP={ATP}")

# Simulate Electron Transport Chain
ATP_etc = electron_transport_chain(NADH, FADH2)
ATP += ATP_etc

print(f"After Electron Transport Chain: ATP={ATP}")

# Final output
print(f"Total ATP produced from one glucose molecule: {ATP}")
