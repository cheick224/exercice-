
	class Adress:

    def __init__(self,codePostal,rue,ville):
        self.__codePostal = codePostal
        self.__ville = ville
        self.__rue = rue
    
    @property
    def codePostal(self):
        return self.__codePostal

    @property
    def ville(self):
        return self.__ville

    @property  
    def rue(self):
        return self.__rue

          @codePostal.setter
    def codePostal(self,v):
        self.__codePostal = v
    
    @ville.setter
    def ville(self,v):
        self.__ville = v
    
    @rue.setter
    def rue(self,r):
        self.__rue = r

    def __str__(self):
        return ("Adress [ville : {} , rue: {} , codePostal: {}] ".format(self.__ville,self.__rue,self.__codePostal))







        ### une autre classe

from personne import Personne
import pickle

class ListPersonnes:

    def __init__(self):
        self.__personnes = []
    
    def addPersonne(self,p):
        self.__personnes.append(p)
    
    def getPersonnes(self):
        return self.__personnes
    
    def removePersonne(self,p):
        if p in self.__personnes :
            self.__personnes.remove(p)
        else:
            print("La personne {} n'existe pas ".format(p))
    
    def find_by_nom(self,s):
        for personne in self.__personnes :
            if personne.nom == str(s) :
                return str(personne)
        return None
    def exists_code_postal(self,c):
        for personne in self.__personnes :
            for adr in personne.getAdress():
                if adr.codePostal == c :
                    return True
                else :
                	return False

    def count_personne_ville(self,ville):
        count = 0
        for personne in self.__personnes :
            for adr in personne.getAdress():
                if adr.ville == ville :
                    count = count + 1
        return count

    def edit_personne_nom(self,oldNom,newNom) :
        for personne in self.__personnes :
            if personne.nom == oldNom:
                personne.nom = newNom

    def edit_personne_ville(self,nom,newVille):
        for personne in self.__personnes :
            if personne.nom == nom:
                for adr in personne.getAdress():
                    adr.ville = newVille

    def __str__(self):
        return ("Liste Personnes : \n {} ".format('\n'.join([str(per) for per in self.__personnes])))

    def write_in_file(self):
        with open("personnes.data","w") as fic:
            for person in self.__personnes:
                fic.write('%s\n' % person)
        print("les personnes sont enregistrées")
        fic.close()
        def read_from_file(self):
        personnes = []
        with open("personnes.data","r") as fic:
            for line in fic:
                personnes.append(line)
        fic.close()
        return personnes
 


 ###une autre classe 
 from adress import Adress
class Personne :

    def __init__(self,nom,sex):
        self.__nom = nom
        self.__sex = sex
        self.__adresses= []

    @property
    def nom(self):
        return self.__nom
    
    @property
    def sex():
        return self.__sex
    
    @nom.setter
    def nom(self,a):
        self.__nom = a
    
    @sex.setter
    def sex(self,s):
        self.__sex = s


    def add_adress(self,adress):
        self.__adresses.append(adress)
        print ("l'adress {} est okay ".format(adress))

    def getAdress(self):
        return self.__adresses
    def removeAdress(self,adress):
        if adress in self.__adresses:
            self.__adresses.remove(adress)
            print ("l'adress {} is delete ".format(adress))
    
    def __str__(self):

        return (' Personne : [nom : {} , sex: {} , adresses: {}]'.format(self.__nom,self.__sex,[str(addr) for addr in self.__adresses] ))
