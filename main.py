from gestionnaire import (
    charger_taches,
    sauvegarder_taches,
    ajouter_tache,
    afficher_taches,
    supprimer_tache,
    marquer_faite,
    supprimer_tache
)

# fonction pour afficher le menu principal
def menu():
    print("\n=== Gestionnaire de Tâches ===")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")

taches = charger_taches()

while True:
    menu()
    choix = input("Choisissez une option: ")

    if choix == "1":
        afficher_taches(taches)

    elif choix == "2":
        titre = input("Titre de la tâche: ")
        description = input("Description de la tâche: ")
        ajouter_tache(taches, titre, description)

    elif choix == "3":
        afficher_taches(taches)
        index = int(input("Numéro de la tâche faite: ")) - 1
        marquer_faite(taches, index)

    elif choix== "4":
        afficher_taches(taches)
        index = int(input("Numéro de la tâche à supprimer")) - 1
        supprimer_tache(taches, index)

    elif choix =="5":
        print("Au revoir Bill !")
        break

    else:
        print("Option invalide. Veuillez réessayer.")


