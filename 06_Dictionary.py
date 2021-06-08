# DICTIONARY IN PYTHON......
# Dictionary is nothing but key value pairs..........
                                                                                #  OUTPUTS
d1 = {}
print(type(d1))

d2 = {"Sambhu":"chaomin",
      "Ankit":"Egg",
      "Rame":"Alu",
      "Bilasini":"Achar",
      "Seema" : {"s":"Achar","B":"MAngo","D":"Tomato","R":"Fruits"}}
print(d2["Rame"])                                                               #  Alu
print(d2["Seema"])                                                              # {'Achar', 'Tomato', 'MAngo', 'Fruits'}
print(d2["Seema"]["R"])                                                         # Fruits

d2["Chera"] = "Rice"
print(d2)                           # {'Sambhu': 'chaomin', 'Ankit': 'Egg', 'Rame': 'Alu', 'Bilasini': 'Achar', 'Seema': {'s': 'Achar', 'B': 'MAngo', 'D': 'Tomato', 'R': 'Fruits'}, 'Chera': 'Rice'}
d2[2324] = "Money"
print(d2)
del d2["Chera"]
del d2[2324]
del d2["Seema"]
print(d2)                           # {'Sambhu': 'chaomin', 'Ankit': 'Egg', 'Rame': 'Alu', 'Bilasini': 'Achar'}

d2.update({"Sambhu":"Alu"})
print(d2)                           # {'Sambhu': 'Alu', 'Ankit': 'Egg', 'Rame': 'Alu', 'Bilasini': 'Achar'}

print(d2.keys())                    # dict_keys(['Sambhu', 'Ankit', 'Rame', 'Bilasini'])
print(d2.items())                   # dict_items([('Sambhu', 'Alu'), ('Ankit', 'Egg'), ('Rame', 'Alu'), ('Bilasini', 'Achar')])
print(d2.get("Bilasini"))           # Achar


