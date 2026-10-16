n=int(input("Entrez un nombre entier : "))

if n>0 and n%2==0:
    print("Le nombre est positif et pair")
elif n<0 and n%2==0:
    print("Le nombre est negatif et pair")
elif n>0 and n%2==1:
    print("Le nombre est positif et impair")
elif n<0 and n%2==1:
    print("Le nombre est negatif et impair")
else:
    print("Le nombre vaut 0")
