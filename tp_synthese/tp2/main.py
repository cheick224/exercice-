from personne import Personne
from adress import Adress
from listePersonnes import ListPersonnes

print("="*20 + "Create adresses" +"="*20)
print("\n")

adress1 = Adress("99410","vaujours ","saint denis")
adress2 = Adress("93190","livry gagan","saint denis")


print("="*20 + "Creer personne"+"="*20)
print("\n")

personne1 = Personne("cheick","M")
personne2 = Personne("Aicha","F")

print("="*20 + "Ajouter Adresses personne" +"="*14)
print("\n")

personne1.add_adress(adress1)
personne1.add_adress(adress2)
personne2.add_adress(adress3)

print("="*20 + "LIST PERSONS" +"="*20)
print("\n")

print(personne1)

listePersonnes1 = ListPersonnes()
listePersonnes1.addPersonne(personne1)
listePersonnes1.addPersonne(personne2)


print("="*20 + "Update " +"="*20)
print("\n")

listePersonnes1.edit_personne_ville("eddy","douala")
print(listePersonnes1)


print("="*20 + "Update P" +"="*20)
print("\n")

listePersonnes1.edit_personne_nom("kyky","Mbappe")
print(listePersonnes1)

print("\n")
print("="*20 + "Nombre d'objet avec ville 'saint-denis" +"="*20)
print("\n")

number = listePersonnes1.count_personne_ville('saint-denis')
print(number)

print("\n")
print("="*20 + "Exists code Postal 93410" +"="*20)
print("\n")

print(listePersonnes1.exists_code_postal("93410"))

print("\n")
print("="*20 + "Existe deja" +"="*20)
print("\n")

print(listePersonnes1.find_by_nom("eddy"))

print("\n")
print("="*20 + "ecrire dans le fichier" +"="*20)
print("\n")

listePersonnes1.write_in_file()

print("="*20 + "lire du fichier" +"="*20)
print('\n'.join(str(elem) for elem in listePersonnes1.read_from_file()))