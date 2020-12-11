from connection import create_connection,create_table 

new_conn = create_connection("BDD.db")
if new_conn is None:
	raise Exception ("error impossible de creeer la base")
	sql_create_tables = """ CREATE TABLE "Client"{
									"idClient" INTEGER NOT NULL,
									"civiliteCLient" TEXT NOT NULL,
									"nomClient" TEXT NOT NULL,
									"prenomClient" TEXT NOT NULL,
									"adresseClient" VARCHAR NOT NULL,
									PRIMARY KEY("idClient" AUTOINCREMENT)
									);
									CREATE TABLE "CompteBancaire"{
									"idCompte" INTEGER NOT NULL,
									"soldeCompte" INTEGER NOT NULL,
									"decouvertCompte" TEXT NOT NULL,
									PRIMARY KEY("idCompte" AUTOINCREMENT)
									FOREIGN KEY("idClient") REFERENCES "Client"("idClient")
									FOREIGN KEY("idAgence") REFERENCES "Agence"("idAgence")

									);
									CREATE TABLE "Agence"{
									"idAgence" INTEGER NOT NULL,
									"nomAgence" TEXT NOT NULL,
									PRIMARY KEY("idAgence" AUTOINCREMENT)
									);"""


create_table(new_conn,sql_create_tables)

### CRUD
### AJOUTER
def ajouterClient(conn,Client):
	sql = ''' INSERT INTO Client(civiliteClient,nomClient,prenomClient,adresseClient)
	          values(?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql,Client)
	conn.commit()
	return cur.lastrowid
def ajouterCompteBancaire(conn,CompteBancaire):
	sql = ''' INSERT INTO CompteBancaire(soldeCompte,decouvertCompte)
	          values(?,?) '''
	cur = conn.cursor()
	cur.execute(sql,CompteBancaire)
	conn.commit()
	return cur.lastrowid
def ajouterAgence(conn,nomAgence):
	sql = ''' INSERT INTO Client(nomAgence)
	          values(?,) '''
	cur = conn.cursor()
	cur.execute(sql,Agence)
	conn.commit()
	return cur.lastrowid
### SELECT
def listerClient(conn)
    cur= conn.cursor()
    cur.execute("SELECT * FROM Client")
    rows  = cur.fetchall()
    for Client in rows:
    	print(Client)

def listerCompteBancaire(conn)
    cur= conn.cursor()
    cur.execute("SELECT * FROM CompteBancaire")
    rows  = cur.fetchall()
    for CompteBancaire in rows:
    	print(CompteBancaire)

 def listerAgence(conn)
    cur= conn.cursor()
    cur.execute("SELECT * FROM Agence")
    rows  = cur.fetchall()
    for Agence in rows:
    	print(Agence)

 ### MODIFICATION 
def modifierClient(conn,newClient)
    if (newClient['id'] is not None and newClient['civiliteClient'] is not None):
    	sql = ''' UPDATE Client
    	            SET civiliteClient = ?,
    	            nomClient = ?,
    	            prenomClient = ?,
    	            adresse = ?,
    	            WHERE id = ?'''
    	cur = conn.cursor()
    	cur.execute(sql,(newClient['row'],newClient['id']))
    	conn.commit()

def modifierCompteBancaire(conn,newCompteBancaire)
    if (newCompteBancaire['id'] is not None and newCompteBancaire['soldeCompte'] is not None):
    	sql = ''' UPDATE CompteBancaire
    	            SET solde= ?,
    	            decouvert= ?,
    	            WHERE id = ?'''
    	cur = conn.cursor()
    	cur.execute(sql,(newCompteBancaire['row'],newCompteBancaire['id']))
    	conn.commit()
def modifierAgence(conn,newAgence)
    if (newAgence['id'] is not None and newAgence['nomAgence'] is not None):
    	sql = ''' UPDATE Agence
    	            SET nomAgence= ?,
    	            WHERE id = ?'''
    	cur = conn.cursor()
    	cur.execute(sql,(newAgence['row'],newAgence['id']))
    	conn.commit()

#### SUPPRESION
def supprimerClient(conn,idClient):
     sql ='DELETE FROM Client WHERE id=?'
     cur = conn.cursor()
     cur.execute(sql, (idClient,))
     conn.commit()

def supprimerCompteBancaire(conn,idCompte):
     sql ='DELETE FROM CompteBancaire WHERE id=?'
     cur = conn.cursor()
     cur.execute(sql, (idCompte,))
     conn.commit() 

def supprimerAgence(conn,idAgence):
     sql ='DELETE FROM Agence WHERE id=?'
     cur = conn.cursor()
     cur.execute(sql, (idAgence,))
     conn.commit() 

 ### LISTER AGENCE & COMPTES 
def listerAgence(conn):
 	cur = conn.cursor()
 	cur.execute("SELECT * FROM Agence")
 	rows = cur.fetchall()
 	for Agence in rows:
 		print(Agence)

def listerCompteBancaire(conn):
 	cur = conn.cursor()
 	cur.execute("SELECT * FROM CompteBancaire")
 	rows = cur.fetchall()
 	for CompteBancaire in rows:
 		print(CompteBancaire)











