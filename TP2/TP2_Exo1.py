x = int(input("Entrez x : "))
y = int(input("Entrez y : "))

print()
print("Avant permutation : ")
print("x : ", x)
print("y : ", y)

temp = x
x = y
y = temp

print()
print("Après permutation : ")
print("x : ", x)
print("y : ", y)