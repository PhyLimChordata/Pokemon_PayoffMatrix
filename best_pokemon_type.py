types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']

# 2D array where row elements are the defending type and column elements are the offending type
# 0 - Neutral
# 1/2 - Super effective (Advantageous)
# -1/2 - Resistant (Disadvantageous)
# 1 - Immune
matchups = {'normal': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': -1/2, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 1, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'fire': {'normal': 0, 'fire': 1/2, 'water': -1/2, 'grass': 1/2, 'electric': 0, 'ice': 1/2, 'fighting': 0, 'poison': 0, 'ground': -1/2, 'flying': 0, 'psychic': 0, 'bug': 1/2, 'rock': -1/2, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 1/2, 'fairy': 1/2},
           'water': {'normal': 0, 'fire': 1/2, 'water': 1/2, 'grass': -1/2, 'electric': -1/2, 'ice': 1/2, 'fighting': 0, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 1/2, 'fairy': 0},
           'grass': {'normal': 0, 'fire': -1/2, 'water': 1/2, 'grass': 1/2, 'electric': 1/2, 'ice': -1/2, 'fighting': 0, 'poison': -1/2, 'ground': 1/2, 'flying': -1/2, 'psychic': 0, 'bug': -1/2, 'rock': 0, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'electric': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 1/2, 'ice': 0, 'fighting': 0, 'poison': 0, 'ground': -1/2, 'flying': 1/2, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'ice': {'normal': 0, 'fire': -1/2, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 1/2, 'fighting': -1/2, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': -1/2, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': -1/2, 'fairy': 0},
           'fighting': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 0, 'poison': 0, 'ground': 0, 'flying': -1/2, 'psychic': -1/2, 'bug': 1/2, 'rock': 1/2, 'ghost': 0, 'dragon': 0, 'dark': 1/2, 'steel': 0, 'fairy': -1/2},
           'poison': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 1/2, 'electric': 0, 'ice': 0, 'fighting': 1/2, 'poison': 1/2, 'ground': -1/2, 'flying': 0, 'psychic': -1/2, 'bug': 1/2, 'rock': 0, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 1/2},
           'ground': {'normal': 0, 'fire': 0, 'water': -1/2, 'grass': -1/2, 'electric': 1, 'ice': -1/2, 'fighting': 0, 'poison': 1/2, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 1/2, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'flying': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 1/2, 'electric': -1/2, 'ice': -1/2, 'fighting': 1/2, 'poison': 0, 'ground': 1, 'flying': 0, 'psychic': 0, 'bug': 1/2, 'rock': -1/2, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'psychic': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 1/2, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 1/2, 'bug': -1/2, 'rock': 0, 'ghost': -1/2, 'dragon': 0, 'dark': -1/2, 'steel': 0, 'fairy': 0},
           'bug': {'normal': 0, 'fire': -1/2, 'water': 0, 'grass': 1/2, 'electric': 0, 'ice': 0, 'fighting': 1/2, 'poison': 0, 'ground': 1/2, 'flying': -1/2, 'psychic': 0, 'bug': 0, 'rock': -1/2, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': 0, 'fairy': 0},
           'rock': {'normal': 1/2, 'fire': 1/2, 'water': -1/2, 'grass': -1/2, 'electric': 0, 'ice': 0, 'fighting': -1/2, 'poison': 1/2, 'ground': -1/2, 'flying': 1/2, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0, 'dragon': 0, 'dark': 0, 'steel': -1/2, 'fairy': 0},
           'ghost': {'normal': 1, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 1, 'poison': 1/2, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 1/2, 'rock': 0, 'ghost': -1/2, 'dragon': 0, 'dark': -1/2, 'steel': 0, 'fairy': 0},
           'dragon': {'normal': 0, 'fire': 1/2, 'water': 1/2, 'grass': 1/2, 'electric': 1/2, 'ice': -1/2, 'fighting': 0, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 0, 'rock': 0, 'ghost': 0, 'dragon': -1/2, 'dark': 0, 'steel': 0, 'fairy': -1/2},
           'dark': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': -1/2, 'poison': 0, 'ground': 0, 'flying': 0, 'psychic': 1, 'bug': -1/2, 'rock': 0, 'ghost': 1/2, 'dragon': 0, 'dark': 1/2, 'steel': 0, 'fairy': -1/2},
           'steel': {'normal': 1/2, 'fire': -1/2, 'water': 0, 'grass': 1/2, 'electric': 0, 'ice': 1/2, 'fighting': -1/2, 'poison': 1, 'ground': -1/2, 'flying': 1/2, 'psychic': 1/2, 'bug': 1/2, 'rock': 1/2, 'ghost': 0, 'dragon': 1/2, 'dark': 0, 'steel': 1/2, 'fairy': 1/2},
           'fairy': {'normal': 0, 'fire': 0, 'water': 0, 'grass': 0, 'electric': 0, 'ice': 0, 'fighting': 1/2, 'poison': -1/2, 'ground': 0, 'flying': 0, 'psychic': 0, 'bug': 1/2, 'rock': 0, 'ghost': 0, 'dragon': 1, 'dark': 1/2, 'steel': -1/2, 'fairy': 0}
          }

# 2D array where row elements are the defending damage modifier and column elements are the defending type
matchupScore = {1/2: {1/2: 0, 0: 0.5, -1/2: 3/4, 1: 1}, 
                0: {1/2: -1/2, 0: 0, -1/2: 1/2, 1: 1}, 
                -1/2: {1/2: -3/4, 0: -1/2, -1/2: 0, 1: 1},
                1: {1/2: -1, 0: -1, -1/2: -1, 1: 0}}

payoffs = []

for dtype in types:
    for otype in types:
        defense = matchups[dtype][otype]
        offense = matchups[otype][dtype]
      
        score = matchupScore[defense][offense]
        
        print("Offense: " + str(otype) + " Defense: " + str(dtype) + " = " + str(score))
        payoffs.append(str(score) + ", " + str(-score))