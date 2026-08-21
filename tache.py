# initialisation de la classe Tache avec les attributs titre, description et faite
import datetime

class Tache:
    def __init__(self, titre, description, priorite="moyenne", faite=False, date_creation=None):
        self.titre = titre
        self.description = description
        self.priorite = priorite
        self.faite = faite
        self.date_creation = date_creation or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def marquer_faite(self):
        self.faite = True

    def to_dict(self):
        return {
            'titre' : self.titre,
            'description' : self.description,
            'priorite' : self.priorite,
            'faite' : self.faite,
            'date_creation' : self.date_creation
        }
    # méthode statique pour créer une instance de Tache à partir d'un dictionnaire
    @staticmethod
    def from_dict(data):
        return Tache(
            data['titre'],
            data['description'],
            data.get('priorite', 'moyenne'),
            data.get('faite', False),
            data.get('date_creation')
        )




