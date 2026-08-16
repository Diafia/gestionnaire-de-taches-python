import json
from tache import Tache

FICHIER = "taches.json"

# fonction initiale pour charger les tâches depuis le fichier JSON qui a été commentée et remplacée par une version améliorée
""" def charger_taches():
    try:
        with open(FICHIER, 'r') as f:
            data = json.load(f)
            return [Tache.from_dict(t) for t in data]
    except FileNotFoundError:
        return[] """

# fonction améliorée pour charger les tâches depuis le fichier JSON, gérant les cas où le fichier est vide ou contient des données invalides
def charger_taches():
    try:
        with open(FICHIER, 'r', encoding='utf-8') as f:
            contenu = f.read().strip()
            if not contenu:
                return []
            data = json.loads(contenu)
            return [Tache.from_dict(t) for t in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# fonction pour sauvegarder les tâches dans le fichier JSON
def sauvegarder_taches(taches):
    with open(FICHIER, 'w') as f:
        json.dump([t.to_dict() for t in taches], f, indent=4)

# fonctions pour gérer les tâches
def ajouter_tache(taches, titre, description):
    t = Tache(titre, description)
    taches.append(t)
    sauvegarder_taches(taches)

# fonctions pour afficher, marquer comme faite et supprimer les tâches
def afficher_taches(taches):
    if not taches:
        print("Aucune tâches.")
        return
    for i, t in enumerate(taches):
        statut = "FAITE" if t.faite else "NON FAITE"
        print(f"{i+1}.{t.titre} - {statut}\n")
        print(f"{t.description}\n")

def marquer_faite(taches, index):
    try:
        taches[index].marquer_faite()
        sauvegarder_taches(taches)
    except IndexError:
        print("Index invalide.")

def supprimer_tache(taches, index):
    try:
        taches.pop(index)
        sauvegarder_taches(taches)
    except IndexError:
        print("Index invalide.")




