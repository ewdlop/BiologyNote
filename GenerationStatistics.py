import random
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class GeneticTrait:
    def __init__(self, name, inheritance_type, possible_alleles):
        self.name = name
        self.inheritance_type = inheritance_type
        self.possible_alleles = possible_alleles
        
    def express_phenotype(self, allele1, allele2):
        if self.inheritance_type == 'complete':
            return self.complete_dominance(allele1, allele2)
        elif self.inheritance_type == 'incomplete':
            return self.incomplete_dominance(allele1, allele2)
        else:  # codominant
            return self.codominance(allele1, allele2)
    
    def complete_dominance(self, allele1, allele2):
        if allele1.isupper() or allele2.isupper():
            return f"Dominant {self.name}"
        return f"Recessive {self.name}"
    
    def incomplete_dominance(self, allele1, allele2):
        if allele1.isupper() and allele2.isupper():
            return f"High {self.name}"
        elif allele1.islower() and allele2.islower():
            return f"Low {self.name}"
        else:
            return f"Medium {self.name}"
    
    def codominance(self, allele1, allele2):
        if allele1 == allele2:
            return f"Pure {allele1}"
        return f"Mixed {allele1}/{allele2}"

class Organism:
    def __init__(self, traits, generation=0):
        self.genotype = {}
        self.traits = traits
        self.generation = generation
        self.fitness = 1.0
        
    def set_genotype(self, trait_name, allele1, allele2):
        self.genotype[trait_name] = (allele1, allele2)
    
    def get_phenotype(self):
        phenotype = []
        for trait_name, trait in self.traits.items():
            allele1, allele2 = self.genotype[trait_name]
            phenotype.append(trait.express_phenotype(allele1, allele2))
        return " | ".join(phenotype)
    
    def get_genotype_string(self):
        return " | ".join([f"{trait}: {alleles[0]}{alleles[1]}" 
                          for trait, alleles in self.genotype.items()])

class Population:
    def __init__(self, traits, size=100):
        self.traits = traits
        self.size = size
        self.generations = []
        self.create_initial_population()
    
    def create_initial_population(self):
        initial_gen = []
        for _ in range(self.size):
            org = Organism(self.traits)
            for trait_name, trait in self.traits.items():
                allele1 = random.choice(trait.possible_alleles)
                allele2 = random.choice(trait.possible_alleles)
                org.set_genotype(trait_name, allele1, allele2)
            initial_gen.append(org)
        self.generations.append(initial_gen)
    
    def evolve(self, num_generations):
        for gen in range(num_generations):
            next_gen = []
            for _ in range(self.size):
                parent1 = random.choice(self.generations[-1])
                parent2 = random.choice(self.generations[-1])
                offspring = self.mate(parent1, parent2, gen + 1)
                next_gen.append(offspring)
            self.generations.append(next_gen)
    
    def mate(self, parent1, parent2, generation):
        offspring = Organism(self.traits, generation)
        
        for trait_name in self.traits:
            p1_allele1, p1_allele2 = parent1.genotype[trait_name]
            p2_allele1, p2_allele2 = parent2.genotype[trait_name]
            
            offspring_allele1 = random.choice([p1_allele1, p1_allele2])
            offspring_allele2 = random.choice([p2_allele1, p2_allele2])
            
            offspring.set_genotype(trait_name, offspring_allele1, offspring_allele2)
        
        return offspring
    
    def get_generation_stats(self, generation_idx):
        generation = self.generations[generation_idx]
        phenotypes = [org.get_phenotype() for org in generation]
        genotypes = [org.get_genotype_string() for org in generation]
        
        return {
            'phenotype_frequencies': Counter(phenotypes),
            'genotype_frequencies': Counter(genotypes),
            'generation_number': generation_idx
        }

def visualize_population(population, trait_name):
    all_phenotypes = []
    generation_numbers = []
    
    for gen_idx, generation in enumerate(population.generations):
        phenotypes = [org.get_phenotype() for org in generation]
        all_phenotypes.extend(phenotypes)
        generation_numbers.extend([gen_idx] * len(phenotypes))
    
    df = pd.DataFrame({
        'Generation': generation_numbers,
        'Phenotype': all_phenotypes
    })
    
    plt.figure(figsize=(15, 8))
    sns.countplot(data=df, x='Generation', hue='Phenotype')
    plt.title(f'Phenotype Distribution Across Generations')
    plt.xlabel('Generation')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Example usage
traits = {
    'eyes': GeneticTrait('Eyes', 'complete', ['B', 'b']),
    'height': GeneticTrait('Height', 'incomplete', ['T', 't']),
    'petals': GeneticTrait('Petals', 'codominant', ['R', 'W'])
}

# Create and evolve population
pop = Population(traits, size=100)
pop.evolve(5)

# Visualize results
visualize_population(pop, 'all')

# Print detailed statistics for final generation
final_stats = pop.get_generation_stats(-1)
print("\nFinal Generation Statistics:")
print("\nPhenotype Frequencies:")
for phenotype, count in final_stats['phenotype_frequencies'].most_common():
    percentage = (count / pop.size) * 100
    print(f"{phenotype}: {percentage:.1f}%")

print("\nGenotype Frequencies:")
for genotype, count in final_stats['genotype_frequencies'].most_common():
    percentage = (count / pop.size) * 100
    print(f"{genotype}: {percentage:.1f}%")
