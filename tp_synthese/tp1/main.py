from  BDD import *

new_conn = create_connection("BDD.db")
if new_conn is None 
      raise Exception("Error <impossible imposible connection ")

ajouterClient(new_conn,'Monsiuer','cheick','MOMO','PARIS_SUD')
ajouterCompteBancaire(new_conn,'85145','decouvert')
ajouterAgence(new_conn,'PARIS_CIC')
