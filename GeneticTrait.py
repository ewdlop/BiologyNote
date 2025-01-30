import random
from collections import Counter

class GeneticTrait:
    def __init__(self, name, inheritance_type):
        self.name = name
        self.inheritance_type = inheritance_type  # 'complete', 'incomplete', or 'codominant'
        
    def express_phenotype(self, allele1, allele2):
        if self.inheritance_type == 'complete':
            return self.complete_dominance(allele1, allele2)
        elif self.inheritance_type == 'incomplete':
            return self.incomplete_dominance(allele1, allele2)
        else:  # codominant
            return self.codominance(allele1, allele2)
    
    def complete_dominance(self, allele1, allele2):
        # Assuming capital letters are dominant
        if allele1.isupper() or allele2.isupper():
            return f"{self.name}: {allele1.upper()}"
        return f"{self.name}: {allele1.lower()}"
    
    def incomplete_dominance(self, allele1, allele2):
        if allele1.isupper() and allele2.isupper():
            return f"{self.name}: Tall"
        elif allele1.islower() and allele2.islower():
            return f"{self.name}: Short"
        else:
            return f"{self.name}: Medium"
    
    def codominance(self, allele1, allele2):
        if allele1 == allele2:
            return f"{self.name}: {allele1}"
        return f"{self.name}: {allele1}/{allele2}"

class Organism:
    def __init__(self, traits):
        self.genotype = {}
        self.traits = traits
        
    def set_genotype(self, trait_name, allele1, allele2):
        self.genotype[trait_name] = (allele1, allele2)
    
    def get_phenotype(self):
        phenotype = []
        for trait_name, trait in self.traits.items():
            allele1, allele2 = self.genotype[trait_name]
            phenotype.append(trait.express_phenotype(allele1, allele2))
        return " | ".join(phenotype)

def create_gamete(organism, trait_name):
    allele1, allele2 = organism.genotype[trait_name]
    return random.choice([allele1, allele2])

def mate(parent1, parent2):
    offspring = Organism(parent1.traits)
    
    for trait_name in parent1.traits:
        gamete1 = create_gamete(parent1, trait_name)
        gamete2 = create_gamete(parent2, trait_name)
        offspring.set_genotype(trait_name, gamete1, gamete2)
    
    return offspring

# Set up traits
traits = {
    'eyes': GeneticTrait('Eyes', 'complete'),
    'height': GeneticTrait('Height', 'incomplete'),
    'petals': GeneticTrait('Petals', 'codominant')
}

# Create parent organisms
parent1 = Organism(traits)
parent2 = Organism(traits)

# Set genotypes for parents
parent1.set_genotype('eyes', 'B', 'B')    # BB
parent1.set_genotype('height', 'T', 't')  # Tt
parent1.set_genotype('petals', 'R', 'W')  # RW

parent2.set_genotype('eyes', 'B', 'b')    # Bb
parent2.set_genotype('height', 't', 't')  # tt
parent2.set_genotype('petals', 'R', 'R')  # RR

# Simulate multiple offspring
num_offspring = 1000
offspring_phenotypes = []

for _ in range(num_offspring):
    offspring = mate(parent1, parent2)
    offspring_phenotypes.append(offspring.get_phenotype())

# Count phenotype frequencies
phenotype_counts = Counter(offspring_phenotypes)

print("Parent 1 phenotype:", parent1.get_phenotype())
print("Parent 2 phenotype:", parent2.get_phenotype())
print("\nOffspring phenotype distributions:")
for phenotype, count in phenotype_counts.items():
    percentage = (count / num_offspring) * 100
    print(f"{phenotype}: {percentage:.1f}%")
