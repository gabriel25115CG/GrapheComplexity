# performance.py
import time
import matplotlib.pyplot as plt
from dijkstra import dijkstra_naif, dijkstra_tas
from utils import generer_graphe_aleatoire
from typing import List, Tuple

def comparer_performances(tailles_graphes: List[int], densite: float = 0.3) -> Tuple[List[float], List[float], List[int], List[int]]:
    temps_naif = []
    temps_tas = []
    operations_naif = []
    operations_tas = []
    
    for n in tailles_graphes:
        nb_aretes = int(densite * n * (n - 1) / 2)
        nb_aretes = max(nb_aretes, n - 1)
        
        graphe = generer_graphe_aleatoire(n, nb_aretes)
        
        debut = time.time()
        _, _, operations_n, comparisons_n = dijkstra_naif(graphe, 0)
        temps_naif.append(time.time() - debut)
        operations_naif.append(operations_n + comparisons_n)
        
        debut = time.time()
        _, _, operations_t, comparisons_t = dijkstra_tas(graphe, 0)
        temps_tas.append(time.time() - debut)
        operations_tas.append(operations_t + comparisons_t)
        
    return temps_naif, temps_tas, operations_naif, operations_tas

def visualiser_performances():
    tailles = [10, 50, 100, 200, 300, 400, 500]
    temps_naif, temps_tas, operations_naif, operations_tas = comparer_performances(tailles)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].plot(tailles, temps_naif, 'o-', label='Dijkstra naïf')
    axes[0].plot(tailles, temps_tas, 'o-', label='Dijkstra avec tas')
    axes[0].set_xlabel('Nombre de sommets')
    axes[0].set_ylabel('Temps d\'exécution (secondes)')
    axes[0].set_title('Comparaison du temps d\'exécution')
    axes[0].legend()
    axes[0].grid(True)
    
    axes[1].plot(tailles, operations_naif, 'o-', label='Dijkstra naïf')
    axes[1].plot(tailles, operations_tas, 'o-', label='Dijkstra avec tas')
    axes[1].set_xlabel('Nombre de sommets')
    axes[1].set_ylabel('Nombre d\'opérations')
    axes[1].set_title('Comparaison du nombre d\'opérations')
    axes[1].legend()
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()
