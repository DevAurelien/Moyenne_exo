
chemin = "etudiant.txt"
dictionnaire_objet = {}

with open(chemin, "r") as f:
    document = f.readlines()


class Etudiant():
    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes
        self.moyenne = self.moyenne_eleve()

    def moyenne_eleve(self) -> int:
        return round(sum(int(element) for element in self.notes) / len(self.notes))


for eleve in document:
    classeur = "".join("".join(eleve.split("->")).split(",")).split()  # separate string
    nom_etudiant = classeur.pop(0)
    dictionnaire_objet[nom_etudiant] = Etudiant(nom_etudiant, classeur)  # create studients instances in dictionnary

dico_moyenne = {cle: dictionnaire_objet[cle].moyenne for cle in dictionnaire_objet.keys()}


def classement_eleves(dico_moyenne):
    dico_2 = sorted(dico_moyenne.items(), key=lambda t: t[1], reverse=True)
    return "\n".join([f"{i + 1:2} : {dico_2[i][0]} avec une moyenne de {dico_2[i][1]}/20" for i in range(len(dico_2))])


if __name__ == "__main__":
    print("\n", dico_moyenne)
    print()
    print(classement_eleves(dico_moyenne))


