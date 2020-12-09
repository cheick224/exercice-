from sqlite3 import *

connection = connect("base.db")
cursor = connection.cursor()
new_etudiant = (cursor.lastrowid, "toto", "tuitui",25)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)', new_etudiant)
connection.commit()
print("c'est bon l'ajout")
"""
cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())
"""
"""
mon_etudiant =1,
cursor.execute('SELECT * FROM etudiant WHERE id=?',mon_etudiant)
print(cursor.fetchone())
"""
modif_etudiant=('dodo','dada',28,1)
cursor.execute('UPDATE etudiant SET nom=?, prenom=?,age=? WHERE id=?',modif_etudiant)
connection.commit()
print("MAJ okay")
cursor.close()
connection.close()