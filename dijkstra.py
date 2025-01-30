# Importation des modules nécessaires
from heapq import heappush, heappop  # Pour utiliser une file de priorité (tas)
from graphe import GrapheNonOriente  # Importation de la structure de graphe
from typing import Dict, Tuple  # Pour les annotations de type

def dijkstra_naif(graphe: GrapheNonOriente, depart: int) -> Tuple[Dict[int, float], Dict[int, int], int, int]:
    """
    Implémente l'algorithme de Dijkstra en utilisant une recherche naive du sommet le plus proche.
    
    :param graphe: Un graphe non orienté avec une structure d'adjacence.
    :param depart: Le sommet de départ.
    :return: Un tuple contenant :
        - Un dictionnaire des distances minimales depuis le départ.
        - Un dictionnaire des prédécesseurs pour reconstruire les chemins.
        - Le nombre total d'opérations effectuées.
        - Le nombre total de comparaisons effectuées.
    """
    # Initialisation des distances à l'infini sauf pour le sommet de départ
    distances = {sommet: float('inf') for sommet in graphe.obtenir_sommets()}
    predecesseurs = {sommet: None for sommet in graphe.obtenir_sommets()}
    distances[depart] = 0
    non_visites = set(graphe.obtenir_sommets())  # Ensemble des sommets non encore visités
    
    operations = 0
    comparisons = 0

    while non_visites:
        # Sélection du sommet avec la plus petite distance actuelle (approche naive O(n))
        sommet_courant = min(non_visites, key=lambda x: distances[x])
        operations += 1
        comparisons += len(non_visites)
        
        # Si la distance est infinie, alors les sommets restants sont inaccessibles
        if distances[sommet_courant] == float('inf'):
            break
            
        # Marquer le sommet comme visité
        non_visites.remove(sommet_courant)
        
        # Mise à jour des distances des voisins
        for voisin, poids in graphe.adjacence[sommet_courant].items():
            if voisin in non_visites:
                distance = distances[sommet_courant] + poids
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    predecesseurs[voisin] = sommet_courant
                    operations += 1
                    comparisons += 1
                    
    return distances, predecesseurs, operations, comparisons

def dijkstra_tas(graphe: GrapheNonOriente, depart: int) -> Tuple[Dict[int, float], Dict[int, int], int, int]:
    """
    Implémente l'algorithme de Dijkstra en utilisant un tas binaire (file de priorité).
    
    :param graphe: Un graphe non orienté avec une structure d'adjacence.
    :param depart: Le sommet de départ.
    :return: Un tuple contenant :
        - Un dictionnaire des distances minimales depuis le départ.
        - Un dictionnaire des prédécesseurs pour reconstruire les chemins.
        - Le nombre total d'opérations effectuées.
        - Le nombre total de comparaisons effectuées.
    """
    # Initialisation des distances à l'infini sauf pour le sommet de départ
    distances = {sommet: float('inf') for sommet in graphe.obtenir_sommets()}
    predecesseurs = {sommet: None for sommet in graphe.obtenir_sommets()}
    distances[depart] = 0
    
    # Utilisation d'un tas binaire pour stocker les sommets à explorer
    tas = [(0, depart)]  # (distance, sommet)
    visites = set()  # Ensemble des sommets déjà traités
    operations = 0
    comparisons = 0

    while tas:
        # Extraction du sommet avec la plus petite distance (logarithmique O(log n))
        distance_courante, sommet_courant = heappop(tas)
        operations += 1
        
        # Vérifier si le sommet a déjà été traité
        if sommet_courant in visites:
            continue
        
        visites.add(sommet_courant)
        
        # Mise à jour des distances des voisins
        for voisin, poids in graphe.adjacence[sommet_courant].items():
            if voisin not in visites:
                distance = distance_courante + poids
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    predecesseurs[voisin] = sommet_courant
                    heappush(tas, (distance, voisin))  # Ajouter le voisin au tas
                    operations += 1
                    comparisons += 1
                    
    return distances, predecesseurs, operations, comparisons
