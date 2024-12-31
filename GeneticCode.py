class GeneticTreeMapper:
   def __init__(self, tree_of_life, genetic_code):
       self.tree = tree_of_life
       self.genetic = genetic_code
       
   def map_sequences(self, node):
       """Map genetic sequences to tree nodes"""
       sequence_data = {
           'dna': node.dna_sequence,
           'rna': self.transcribe(node.dna_sequence),
           'proteins': self.genetic.translate(node.rna_sequence),
           'mutations': self.find_mutations(node)
       }
       node.genetic_data = sequence_data
       
       for child in node.children:
           self.map_sequences(child)
           
   def calculate_distance(self, node1, node2):
       """Calculate genetic distance between species"""
       return {
           'nucleotide_diff': self.nucleotide_distance(
               node1.genetic_data['dna'],
               node2.genetic_data['dna']
           ),
           'amino_acid_diff': self.protein_distance(
               node1.genetic_data['proteins'],
               node2.genetic_data['proteins']
           )
       }
       
   def find_mutations(self, node):
       if not node.parent:
           return []
           
       return [{
           'position': i,
           'parent': node.parent.genetic_data['dna'][i],
           'child': node.genetic_data['dna'][i],
           'type': self.mutation_type(
               node.parent.genetic_data['dna'][i],
               node.genetic_data['dna'][i]
           )
       } for i in range(len(node.genetic_data['dna']))
       if node.genetic_data['dna'][i] != node.parent.genetic_data['dna'][i]]


class GeneticCode:
   def __init__(self):
       self.codon_table = {
           'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
           'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
           'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
           'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V'
       }
       self.amino_properties = {
           'A': {'hydrophobic': True, 'size': 'small'},
           'R': {'charged': True, 'polar': True},
           'N': {'polar': True, 'size': 'medium'},
           'D': {'charged': True, 'acidic': True}
       }

   def translate(self, rna_sequence):
       """Translate RNA to amino acid sequence"""
       proteins = []
       start = 'AUG'
       stops = ['UAA', 'UAG', 'UGA']
       
       i = 0
       while i < len(rna_sequence)-2:
           codon = rna_sequence[i:i+3]
           if codon == start:
               protein = ''
               j = i
               while j < len(rna_sequence)-2:
                   current = rna_sequence[j:j+3]
                   if current in stops:
                       proteins.append(protein)
                       break
                   protein += self.codon_table.get(current, 'X')
                   j += 3
           i += 3
       return proteins

   def analyze_peptide(self, peptide):
       """Analyze amino acid properties"""
       properties = {
           'length': len(peptide),
           'hydrophobic_ratio': sum(
               1 for aa in peptide 
               if self.amino_properties[aa].get('hydrophobic', False)
           ) / len(peptide),
           'charge': sum(
               1 if self.amino_properties[aa].get('charged', False) else 0
               for aa in peptide
           )
       }
       return properties
