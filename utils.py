import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from typing import List
from graphe import GrapheNonOriente


def generer_graphe_aleatoire(nb_sommets: int, nb_aretes: int, *, poids_min: float = 1.0, poids_max: float = 10.0) -> GrapheNonOriente:
    """
    Génère un graphe non orienté aléatoire avec un nombre donné de sommets et d'arêtes.
    
    :param nb_sommets: Nombre total de sommets dans le graphe.
    :param nb_aretes: Nombre total d'arêtes à générer.
    :param poids_min: Poids minimal des arêtes.
    :param poids_max: Poids maximal des arêtes.
    :return: Un objet GrapheNonOriente représentant le graphe généré.
    """
    # Vérifie que le nombre d'arêtes permet de garantir la connexité du graphe
    if nb_aretes < nb_sommets - 1:
        raise ValueError("Le nombre d'arêtes doit être au moins n-1 pour assurer un graphe connexe.")
    
    # Vérifie que le nombre d'arêtes demandé ne dépasse pas le maximum possible dans un graphe non orienté
    max_aretes = (nb_sommets * (nb_sommets - 1)) // 2  # Formule pour un graphe complet
    if nb_aretes > max_aretes:
        raise ValueError(f"Trop d'arêtes demandées. Maximum possible: {max_aretes}")
    
    # Création d'un graphe vide
    graphe = GrapheNonOriente()
    
    # Ajout de tous les sommets au graphe
    for i in range(nb_sommets):
        graphe.ajouter_sommet(i)
        
    # Création d'un arbre couvrant minimal pour assurer la connexité
    sommets_connectes = {0}  # Commence avec le premier sommet
    sommets_non_connectes = set(range(1, nb_sommets))  # Les autres sommets sont initialement non connectés
    
    while sommets_non_connectes:
        # Choisir aléatoirement un sommet déjà connecté et un sommet non connecté
        sommet1 = np.random.choice(list(sommets_connectes))
        sommet2 = np.random.choice(list(sommets_non_connectes))
        
        # Générer un poids aléatoire pour l'arête
        poids = np.random.uniform(poids_min, poids_max)
        
        # Ajouter l'arête au graphe
        graphe.ajouter_arete(sommet1, sommet2, poids)
        
        # Mettre à jour les ensembles de sommets connectés et non connectés
        sommets_connectes.add(sommet2)
        sommets_non_connectes.remove(sommet2)
        
    # Ajout des arêtes restantes jusqu'à atteindre le nombre demandé
    aretes_ajoutees = nb_sommets - 1  # On a déjà ajouté (n-1) arêtes pour garantir la connexité
    
    while aretes_ajoutees < nb_aretes:
        # Sélectionne deux sommets distincts aléatoires
        sommet1, sommet2 = np.random.choice(nb_sommets, 2, replace=False)
        
        # Vérifie si une arête existe déjà entre ces deux sommets
        if sommet2 not in graphe.adjacence[sommet1]:
            poids = np.random.uniform(poids_min, poids_max)
            graphe.ajouter_arete(sommet1, sommet2, poids)
            aretes_ajoutees += 1  # Incrémente le compteur d'arêtes ajoutées
    
    return graphe


def afficher_graphes_cote_a_cote(tailles_graphes: List[int], *, densite: float = 0.3, poids_min: float = 1.0, poids_max: float = 10.0):
    """
    Génère et affiche plusieurs graphes aléatoires côte à côte en fonction des tailles spécifiées.
    
    :param tailles_graphes: Liste des tailles de graphes (nombre de sommets) à générer et afficher.
    :param densite: Densité du graphe (proportion des arêtes par rapport au graphe complet).
    :param poids_min: Poids minimal des arêtes.
    :param poids_max: Poids maximal des arêtes.
    """
    n = len(tailles_graphes)  # Nombre de graphes à afficher
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))  # Création d'une figure avec n sous-graphiques
    
    # Si un seul graphe doit être affiché, s'assurer que axes est une liste
    if n == 1:
        axes = [axes]
    
    for i, taille in enumerate(tailles_graphes):
        # Calcul du nombre d'arêtes en fonction de la densité choisie
        nb_aretes = int(densite * taille * (taille - 1) / 2)  # Formule pour un graphe complet
        nb_aretes = max(nb_aretes, taille - 1)  # S'assure qu'on a au moins (n-1) arêtes pour la connexité
        
        # Génération du graphe aléatoire
        graphe = generer_graphe_aleatoire(taille, nb_aretes, poids_min=poids_min, poids_max=poids_max)
        
        # Création d'un graphe NetworkX pour la visualisation
        G = nx.Graph()
        
        # Ajout des arêtes et des poids au graphe NetworkX
        for sommet1, voisins in graphe.adjacence.items():
            for sommet2, poids in voisins.items():
                G.add_edge(sommet1, sommet2, weight=poids)
        
        # Disposition des nœuds du graphe (spring_layout donne une disposition plus naturelle)
        pos = nx.spring_layout(G)
        
        # Dessin du graphe
        nx.draw(G, pos, ax=axes[i], with_labels=True, node_color='lightblue', node_size=500)
        
        # Ajout des poids des arêtes sur l'affichage
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=axes[i])
        
        # Définition du titre du sous-graphe
        axes[i].set_title(f'Graphe avec {taille} sommets')
    
    # Ajustement de l'affichage pour éviter le chevauchement des sous-graphes
    plt.tight_layout()
    
    # Affichage de la figure contenant tous les graphes générés
    plt.show()
