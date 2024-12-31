# BiologyNote

> <em>Kiss me hard before you go
  Summertime sadness
  I just wanted you to know
  That, baby, you the best
  I got my red dress on tonight
  Dancin' in the dark, in the pale moonlight
  Done my hair up real big, beauty queen style
  High heels off, I'm feelin' alive
  Oh my God, I feel it in the air
  Telephone wires above are sizzlin' like a snare
  Honey, I'm on fire, I feel it everywhere
  Nothin' scares me anymore (one, two, three, four)
  Kiss me hard before you go
  Summertime sadness
  I just wanted you to know
  That, baby, you the best
  I got that summertime, summertime sadness
  Su-su-summertime, summertime sadness
  Got that summertime, summertime sadness
  Oh, oh-oh, oh-oh
  I'm feelin' electric tonight
  Cruisin' down the coast, goin' 'bout 99
  Got my bad baby by my heavenly side
  I know if I go, I'll die happy tonight
  Oh my God, I feel it in the air
  Telephone wires above are sizzlin' like a snare
  Honey, I'm on fire, I feel it everywhere
  Nothin' scares me anymore (one, two, three, four)
  Kiss me hard before you go
  Summertime sadness
  I just wanted you to know
  That, baby, you the best
  I got that summertime, summertime sadness
  Su-su-summertime, summertime sadness
  Got that summertime, summertime sadness
  Oh, oh-oh, oh-oh
  Think I'll miss you forever
  Like the stars miss the sun in the morning sky
  Later's better than never
  Even if you're gone, I'm gonna drive (drive), drive
  I got that summertime, summertime sadness
  Su-su-summertime, summertime sadness
  Got that summertime, summertime sadness
  Oh, oh-oh, oh-oh
  Kiss me hard before you go
  Summertime sadness
  I just wanted you to know
  That, baby, you the best
  I got that summertime, summertime sadness
  Su-su-summertime, summertime sadness
  Got that summertime, summertime sadness
  Oh, oh-oh, oh-oh</em>

# How far away are Americans from Aliens

from aliens import *

```python
class AlienComparison:
   def __init__(self, genetic_code, tree_of_life):
       self.genetic = genetic_code
       self.tree = tree_of_life
       # Common features to look for
       self.universal_traits = {
           'dna_based': True,
           'carbon_based': True,
           'protein_synthesis': True,
           'cell_structure': ['membrane', 'metabolism'],
           'genetic_code': 'universal' # Amino acid encoding
       }
       
   def estimate_divergence(self, alien_data):
       """Estimate evolutionary distance between humans and aliens"""
       differences = {
           'genetic': self._compare_genetic(alien_data),
           'biochemical': self._compare_biochemistry(alien_data),
           'cellular': self._compare_cells(alien_data),
           'complexity': self._compare_complexity(alien_data)
       }
       
       # Convert to billion years based on molecular clock
       return self._calculate_divergence_time(differences)
       
   def _compare_genetic(self, alien_data):
       if not alien_data.get('dna_based'):
           return float('inf')
           
       human_dna = self.tree.get_node('Homo sapiens').genetic_data
       return {
           'sequence_similarity': self._sequence_alignment(
               human_dna, alien_data['genetic_sequence']
           ),
           'code_compatibility': self._compare_genetic_code(
               self.genetic.codon_table,
               alien_data['genetic_code']
           )
       }
       
   def _calculate_divergence_time(self, differences):
       """Calculate divergence time in billion years"""
       if differences['genetic'] == float('inf'):
           return '>4.5' # Different origin
           
       mutation_rate = 2.2e-9 # per site per year
       return differences['genetic']['sequence_similarity'] / mutation_rate / 1e9

```
# How far away are China away from America

class GeographicDistance:
   def __init__(self):
       self.cities = {
           'US': {
               'Washington_DC': (38.8951, -77.0364),
               'NY': (40.7128, -74.0060),
               'LA': (34.0522, -118.2437)
           },
           'China': {
               'Beijing': (39.9042, 116.4074),
               'Shanghai': (31.2304, 121.4737),
               'Guangzhou': (23.1291, 113.2644)
           }
       }

   def calculate_distances(self):
       distances = {}
       for us_city, us_coords in self.cities['US'].items():
           for cn_city, cn_coords in self.cities['China'].items():
               distance = self._haversine(us_coords, cn_coords)
               distances[f"{us_city}-{cn_city}"] = distance
       return distances

   def _haversine(self, coord1, coord2):
       """Calculate great-circle distance between points"""
       lat1, lon1 = coord1
       lat2, lon2 = coord2
       R = 6371 # Earth's radius in kilometers

       dlat = math.radians(lat2 - lat1)
       dlon = math.radians(lon2 - lon1)
       lat1 = math.radians(lat1)
       lat2 = math.radians(lat2)

       a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
       c = 2*math.asin(math.sqrt(a))
       return R * c


# How far away is America from extinction? 2012
<img width="1895" alt="Screenshot 2024-02-01 010111" src="https://github.com/ewdlop/BiologyNote/assets/25368970/c6b3f95d-2fb0-4837-92d6-0df3044bd006">


class TaiwanChineseDistance:
   def __init__(self):
       self.geographic = {
           'Taiwan': (23.5937, 120.9605),
           'China': (35.8617, 104.1954),
           'min_strait_width': 130  # km at narrowest point
       }
       
       self.genetic_distances = {
           'han_chinese_groups': {
               'min_fst': 0.001,  # Minimal genetic differentiation
               'max_fst': 0.019   # Small but measurable differences
           },
           'indigenous_taiwanese': {
               'austronesian_fst': 0.12  # Larger differentiation
           }
       }
       
   def calculate_physical_distance(self):
       return {
           'strait_width': self.geographic['min_strait_width'],
           'capital_distance': self._haversine(
               self.geographic['Taiwan'],
               self.geographic['China']
           )
       }
       
   def analyze_genetic_distance(self, population='han'):
       if population == 'han':
           return self.genetic_distances['han_chinese_groups']
       return self.genetic_distances['indigenous_taiwanese']
       
   def _haversine(self, coord1, coord2):
       """Calculate great-circle distance between points"""
       lat1, lon1 = coord1
       lat2, lon2 = coord2
       R = 6371
       
       dlat = math.radians(lat2 - lat1)
       dlon = math.radians(lon2 - lon1)
       lat1 = math.radians(lat1)
       lat2 = math.radians(lat2)

       a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
       c = 2*math.asin(math.sqrt(a))
       return R * c


# Space-Time-... between US


