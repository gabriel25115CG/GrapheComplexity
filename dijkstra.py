# dijkstra.py
from heapq import heappush, heappop
from graphe import GrapheNonOriente
from typing import Dict, Tuple

def dijkstra_naif(graphe: GrapheNonOriente, depart: int) -> Tuple[Dict[int, float], Dict[int, int], int, int]:
    distances = {sommet: float('inf') for sommet in graphe.obtenir_sommets()}
    predecesseurs = {sommet: None for sommet in graphe.obtenir_sommets()}
    distances[depart] = 0
    non_visites = set(graphe.obtenir_sommets())
    
    operations = 0
    comparisons = 0

    while non_visites:
        sommet_courant = min(non_visites, key=lambda x: distances[x])
        operations += 1
        comparisons += len(non_visites)
        
        if distances[sommet_courant] == float('inf'):
            break
            
        non_visites.remove(sommet_courant)
        
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
    distances = {sommet: float('inf') for sommet in graphe.obtenir_sommets()}
    predecesseurs = {sommet: None for sommet in graphe.obtenir_sommets()}
    distances[depart] = 0
    
    tas = [(0, depart)]
    visites = set()
    operations = 0
    comparisons = 0

    while tas:
        distance_courante, sommet_courant = heappop(tas)
        operations += 1
        
        if sommet_courant in visites:
            continue
            
        visites.add(sommet_courant)
        
        for voisin, poids in graphe.adjacence[sommet_courant].items():
            if voisin not in visites:
                distance = distance_courante + poids
                if distance < distances[voisin]:
                    distances[voisin] = distance
                    predecesseurs[voisin] = sommet_courant
                    heappush(tas, (distance, voisin))
                    operations += 1
                    comparisons += 1
                    
    return distances, predecesseurs, operations, comparisons
