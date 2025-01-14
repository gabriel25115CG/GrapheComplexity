# utils.py
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from graphe import GrapheNonOriente
from typing import List, Tuple

def generer_graphe_aleatoire(nb_sommets: int, nb_aretes: int, poids_min: float = 1.0, 
                              poids_max: float = 10.0) -> GrapheNonOriente:
    if nb_aretes < nb_sommets - 1:
        raise ValueError("Le nombre d'arêtes doit être au moins n-1 pour un graphe connexe")
    
    max_aretes = (nb_sommets * (nb_sommets - 1)) // 2
    if nb_aretes > max_aretes:
        raise ValueError(f"Trop d'arêtes demandées. Maximum possible: {max_aretes}")
    
    graphe = GrapheNonOriente()
    for i in range(nb_sommets):
        graphe.ajouter_sommet(i)
    
    sommets_connectes = {0}
    sommets_non_connectes = set(range(1, nb_sommets))
    
    while sommets_non_connectes:
        sommet1 = np.random.choice(list(sommets_connectes))
        sommet2 = np.random.choice(list(sommets_non_connectes))
        poids = np.random.randint(poids_min, poids_max + 1)
        graphe.ajouter_arete(sommet1, sommet2, poids)
        sommets_connectes.add(sommet2)
        sommets_non_connectes.remove(sommet2)
    
    aretes_ajoutees = nb_sommets - 1
    while aretes_ajoutees < nb_aretes:
        sommet1, sommet2 = np.random.choice(nb_sommets, 2, replace=False)
        if sommet2 not in graphe.adjacence[sommet1]:
            poids = np.random.randint(poids_min, poids_max + 1)
            graphe.ajouter_arete(sommet1, sommet2, poids)
            aretes_ajoutees += 1
            
    return graphe

def afficher_graphes_cote_a_cote(tailles_graphes: List[int]):
    n = len(tailles_graphes)
    fig, axes = plt.subplots(1, n, figsize=(15, 5))
    if n == 1:
        axes = [axes]
    
    for i, taille in enumerate(tailles_graphes):
        nb_aretes = int(0.3 * taille * (taille - 1) / 2)
        nb_aretes = max(nb_aretes, taille - 1)

        graphe = generer_graphe_aleatoire(taille, nb_aretes)
        
        ax = axes[i]
        G = nx.Graph()
        
        for sommet1, voisins in graphe.adjacence.items():
            for sommet2, poids in voisins.items():
                G.add_edge(sommet1, sommet2, weight=poids)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, ax=ax)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
        
        ax.set_title(f'Graphe {taille} sommets')

    plt.tight_layout()
    plt.show()
