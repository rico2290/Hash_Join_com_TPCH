from collections import defaultdict

def hashJoin(table1, index1, table2, index2):
    h = defaultdict(list)
    
    # Fase de construção Hash
    for s in table1:
        h[s[index1]].append(s)
    # Fase de Junção quando casa
    return [(s, r) for r in table2 for s in h[r[index2]]]
 
table1 = [(27, "Joana"),
          (18, "Alan"),
          (28, "Gloria"),
          (18, "Paulo"),
          (28, "Alan")]
table2 = [("Joana", "Carvalho"),
          ("Joana", "Loureiro"),
          ("Alan", "Nascimento"),
          ("Alan", "Zombies"),
          ("Rico", "Lima")]
 

for row in hashJoin(table1, 1, table2, 0):
    print(row)
