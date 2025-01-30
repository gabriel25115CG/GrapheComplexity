import time
import matplotlib.pyplot as plt
from utils import generer_graphe_aleatoire, afficher_graphes_cote_a_cote
from dijkstra import dijkstra_naif, dijkstra_tas
from typing import List, Tuple


def comparer_performances(tailles_graphes: List[int], densite: float = 0.3) -> Tuple[List[float], List[float], List[int], List[int]]:
    """
    Compare les performances des algorithmes de Dijkstra (naïf et avec tas) sur des graphes de différentes tailles.

    :param tailles_graphes: Liste des tailles de graphes à tester (nombre de sommets).
    :param densite: Densité du graphe, définissant le nombre d'arêtes.
    :return: Quatre listes contenant respectivement :
             - Les temps d'exécution de Dijkstra naïf.
             - Les temps d'exécution de Dijkstra avec tas.
             - Le nombre d'opérations pour Dijkstra naïf.
             - Le nombre d'opérations pour Dijkstra avec tas.
    """
    # Listes pour stocker les résultats des mesures de performance
    temps_naif = []
    temps_tas = []
    operations_naif = []
    operations_tas = []
    
    # Boucle sur chaque taille de graphe spécifiée
    for n in tailles_graphes:
        # Calcul du nombre d'arêtes en fonction de la densité donnée
        nb_aretes = int(densite * n * (n - 1) / 2)  # Formule pour un graphe non orienté
        nb_aretes = max(nb_aretes, n - 1)  # S'assure qu'il y a au moins n-1 arêtes pour garantir la connexité
        
        # Génération d'un graphe aléatoire avec le nombre de sommets et d'arêtes calculé
        graphe = generer_graphe_aleatoire(n, nb_aretes)

        # Mesure du temps d'exécution et du nombre d'opérations pour Dijkstra naïf
        debut = time.time()
        _, _, operations_n, comparisons_n = dijkstra_naif(graphe, 0)
        temps_naif.append(time.time() - debut)
        operations_naif.append(operations_n + comparisons_n)  # Total des opérations et comparaisons
        
        # Mesure du temps d'exécution et du nombre d'opérations pour Dijkstra avec tas
        debut = time.time()
        _, _, operations_t, comparisons_t = dijkstra_tas(graphe, 0)
        temps_tas.append(time.time() - debut)
        operations_tas.append(operations_t + comparisons_t)

    return temps_naif, temps_tas, operations_naif, operations_tas


def visualiser_performances():
    """
    Génère et affiche des graphiques comparant les performances des deux versions de l'algorithme de Dijkstra.
    - Premier graphique : comparaison du temps d'exécution en fonction du nombre de sommets.
    - Deuxième graphique : comparaison du nombre d'opérations effectuées.
    """
    # Définition des tailles de graphes à tester
    tailles = [10, 50, 100, 200, 300, 400, 500]
    
    # Exécution des tests de performance
    temps_naif, temps_tas, operations_naif, operations_tas = comparer_performances(tailles)
    
    # Création de la figure et des sous-graphiques
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Graphique 1 : Temps d'exécution en fonction du nombre de sommets
    axes[0].plot(tailles, temps_naif, 'o-', label='Dijkstra naïf')
    axes[0].plot(tailles, temps_tas, 'o-', label='Dijkstra avec tas')
    axes[0].set_xlabel('Nombre de sommets')
    axes[0].set_ylabel('Temps d\'exécution (secondes)')
    axes[0].set_title('Comparaison du temps d\'exécution')
    axes[0].legend()
    axes[0].grid(True)

    # Graphique 2 : Nombre d'opérations en fonction du nombre de sommets
    axes[1].plot(tailles, operations_naif, 'o-', label='Dijkstra naïf')
    axes[1].plot(tailles, operations_tas, 'o-', label='Dijkstra avec tas')
    axes[1].set_xlabel('Nombre de sommets')
    axes[1].set_ylabel('Nombre d\'opérations')
    axes[1].set_title('Comparaison du nombre d\'opérations')
    axes[1].legend()
    axes[1].grid(True)

    # Ajuste automatiquement la disposition des graphiques
    plt.tight_layout()
    
    # Affichage des graphiques
    plt.show()
