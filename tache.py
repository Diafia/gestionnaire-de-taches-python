# initialisation de la classe Tache avec les attributs titre, description et faite
class Tache:
    def __init__(self, titre, description, faite=False):
        self.titre = titre
        self.description = description
        self.faite = faite

    def marquer_faite(self):
        self.faite = True

    def to_dict(self):
        return {
            'titre' : self.titre,
            'description' : self.description,
            'faite' : self.faite
        }
    # méthode statique pour créer une instance de Tache à partir d'un dictionnaire
    @staticmethod
    def from_dict(data):
        return Tache(data['titre'], data['description'], data['faite'])




