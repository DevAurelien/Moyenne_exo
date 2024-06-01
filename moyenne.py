deil# Tao = [18, 12, 3, 5, 19]
# Josette = [20, 2, 12, 18, 14]
# Patrick = [2, 4, 6, 18, 17]
# Pema = [3, 19, 15, 3, 12]
# Jean = [0, 9, 8, 8, 4]
# Bixente = [14, 20, 10, 12, 4]
# Paco = [16, 1, 1, 1, 20]
# Chuluun = [15, 6, 17, 20, 15]
# Marie = [16, 4, 16, 20, 12]
# Mohamed = [16, 19, 17, 6, 20]
chemin = "etudiant.txt"
dictionnaire_objet = {}

with open(chemin, "r") as f:
    document = f.readlines()


class Etudiant():
    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes
        self.moyenne = self.moyenne_eleves()

    def moyenne_eleves(self) -> dict:
        moyenne = {}
        resultat = round(sum(int(element) for element in self.notes) / len(self.notes))
        moyenne[self.nom] = resultat
        return moyenne


for eleve in document:
    classeur = "".join("".join(eleve.split("->")).split(",")).split()  # separate string
    nom_etudiant = classeur[0]  # take name
    classeur.pop(0)  # delete name
    dictionnaire_objet[nom_etudiant] = Etudiant(nom_etudiant, classeur)  # create studients instances in dictionnary

dico_moyenne = {}
for cle in dictionnaire_objet.keys():
    dico_moyenne.update(dictionnaire_objet[cle].moyenne)

print(dico_moyenne)


def classement_eleves(dico_moyenne):
    i, compteur = 20, 1
    while not i == 0:
        for key, values in dico_moyenne.items():
            if i==values:
                print(
                f"{compteur} : {key} avec une moyenne de {dico_moyenne[key]}/20")
        i-=1


classement_eleves(dico_moyenne)
