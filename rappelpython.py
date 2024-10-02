age = 27 
print(age)


nom = "Sofian"
print("Bonjour",nom)

a = 2
b = 7
a, b = b, a
print(a,b)

nombre = float(input("Entrez un nombre : "))
if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est nul.")