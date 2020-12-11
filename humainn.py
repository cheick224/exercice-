class ville:
	def __init__(self,nomVille):
		self._nomVille = nomVille
		self._batiment = [] 
	@property
	def nomVille(self):
		return self._nomVille
	@nomVille.setter
	def nomVille(self,v):
		self._nomVille = v 
	def get_batiment(self):
		return self._batiment
	def add_batiment(self,b):
		if b not in self._batiment:
			self._batiment.append(b)
	def remove_batiment(self,b):
		if b in self._batiment
		     self._batiment.remove(b)

	def liste_villes(self):
		return len(self._batiment)


class Batiment(ville):
	def __init__(self,nomBat):
		self._nomBat = nomBat
		self._employes = []
	@property
	def nomBat(self):
		return self._nomVille
	@nomVille.setter
	def nomBat(self,b):
		self._nomVille = b

	def get_employes(self):
		return self._batiment
	def add_employes(self,e):
		if e not in self._employes:
			self._batiment.append(b)
	def remove_employes(self,e):
		if e in self._employes
		     self._employes.remove(e)

	
class Entreprise:
	def __init__(self,nomEntr):
		self._nomEntr = nomEntr
		self._batiment = []
		self._villes = []
		@property
	def nomEntr(self):
		return self._nomEntr
	@nomVille.setter
	def nomEntr(self,e):
		self._nomEntr = e

class Employe:
	def __init__(self,nom,prenom):
		self.nom = nom 
		self.prenom = prenom
		@property
	def nom(self):
		return self._nom
	@nomVille.setter
	def nom(self,n):
		self._nom = n
		@property
	def prenom(self):
		return self._prenom
	@nomVille.setter
	def prenom(self,p):
		self._prenom = p






