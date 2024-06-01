
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
            if i == values:
                print(
                f"{compteur} : {key} avec une moyenne de {dico_moyenne[key]}/20")
                compteur +=1
        i -= 1


classement_eleves(dico_moyenne)
