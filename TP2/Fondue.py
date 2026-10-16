BASE=4
fromage=800.0
eau=2
ail=2
pain=400.0

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut : ")
print(f"-{fromage} gr de fromage")
print(f"-{eau} gr de eau")
print(f"-{ail} gr de ail")
print(f"-{pain} gr de pain")