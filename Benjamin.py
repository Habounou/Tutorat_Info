for i in range(10):
    pass

for item in [1, 200, 3]:
    pass

for cle, valeur in {"a": 1, "b": 2}.items():
    pass


class Eleve:
    def __init__(self, nom=None, prenom=None):
        self.nom = nom
        self.prenom = prenom

eleve1 = Eleve("Alexis")
