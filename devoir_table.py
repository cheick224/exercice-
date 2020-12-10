class item:
	def __init__(self,prix,description):
		self.prix = prix 
		self.description = description
	def __str__(self):
		return "{} \n{}\n{}".format(self.prix,self.description)

class position(item):
	def __init__(self,vie,combien_de_vie):
		item.__init__(self,prix,description)
		self.vie = vie
		self.combien_de_vie = combien_de_vie
		def __str__(self):
			print("")
class argent(item):
	def __init__(self,valeur,combien_de_argent):
		item.__init__(self,prix,description)
		self.valeur = valeur
		self.combien_de_argent = combien_de_argent
		def __str__(self):
			print("")



