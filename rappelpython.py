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


i = 1  
while i <= 5:
    print(i)
    i += 1

# Initialiser la variable pour stocker la somme
somme = 0
i = 2  # Commencer à 2, le premier nombre pair
# Utiliser une boucle while pour parcourir les nombres pairs jusqu'à 100
while i <= 100:
    somme += i  # Ajouter le nombre pair à la somme
    i += 2  # Passer au nombre pair suivant
print("La somme des nombres pairs entre 1 et 100 est :", somme)


def somme(a, b):
    return a + b
resultat = somme(5, 3)
print("La somme est :", resultat)

    