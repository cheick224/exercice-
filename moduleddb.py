from sqlite3 import *
connection = connect("exercice.db")
cursor = connection.cursor()
new_etudiant = (cursor.lastrowid, "toto")
cursor.execute('INSERT INTO Etudiant VALUES(?,?)', new_etudiant)
new_cursus = (cursor.lastrowid, "titi")
cursor.execute('INSERT INTO Cursus VALUES(?,?)', new_cursus)
new_matiere = (cursor.lastrowid, "tata")
cursor.execute('INSERT INTO Matiere VALUES(?,?)', new_matiere)
connection.commit()
print("c'est bon l'ajout")

cursor.execute('SELECT * FROM Matiere')

modif_etudiant=('dada',1)
cursor.execute('UPDATE Etudiant SET nomEtudiant=? WHERE idEtudiant=?',modif_etudiant)
modif_cursus=('dada',1)
"""
cursor.execute('UPDATE Cursus SET nomCurcus=? WHERE idCursus=?',modif_cursus)
modif_matiere=('dada',1)
cursor.execute('UPDATE Matiere SET nomMatiere=? WHERE idMatiere=?',modif_matiere)
"""
connection.commit()
print("MAJ okay")

del_etudiant=3,
cursor.execute('DELETE from Etudiant WHERE id=?',del_etudiant)
del_cursus=3,
cursor.execute('DELETE from Cursus  WHERE id=?',del_cursus)
del_matiere=3,
cursor.execute('DELETE from Matiere WHERE id=?',del_etudiant)

connection.commit()
print("suppression okay")



print(cursor.fetchall())