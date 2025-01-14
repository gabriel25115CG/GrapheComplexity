# graphe.py
from typing import List, Tuple

class GrapheNonOriente:
    def __init__(self):
        """Initialise un graphe non orienté vide utilisant une liste d'adjacence."""
        self.adjacence = {}
        
    def ajouter_sommet(self, sommet: int) -> None:
        """Ajoute un nouveau sommet au graphe."""
        if sommet not in self.adjacence:
            self.adjacence[sommet] = {}
            
    def ajouter_arete(self, sommet1: int, sommet2: int, poids: float) -> None:
        """Ajoute une arête entre deux sommets avec un poids donné."""
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        self.adjacence[sommet1][sommet2] = poids
        self.adjacence[sommet2][sommet1] = poids
        
    def supprimer_sommet(self, sommet: int) -> None:
        """Supprime un sommet et toutes ses arêtes associées."""
        if sommet in self.adjacence:
            for voisin in list(self.adjacence[sommet].keys()):
                del self.adjacence[voisin][sommet]
            del self.adjacence[sommet]
            
    def supprimer_arete(self, sommet1: int, sommet2: int) -> None:
        """Supprime l'arête entre deux sommets."""
        if sommet1 in self.adjacence and sommet2 in self.adjacence:
            if sommet2 in self.adjacence[sommet1]:
                del self.adjacence[sommet1][sommet2]
                del self.adjacence[sommet2][sommet1]
                
    def obtenir_sommets(self) -> List[int]:
        """Retourne la liste des sommets du graphe."""
        return list(self.adjacence.keys())
    
    def obtenir_aretes(self) -> List[Tuple[int, int, float]]:
        """Retourne la liste des arêtes avec leurs poids."""
        aretes = []
        sommets_vus = set()
        for sommet1 in self.adjacence:
            for sommet2, poids in self.adjacence[sommet1].items():
                if (sommet2, sommet1) not in sommets_vus:
                    aretes.append((sommet1, sommet2, poids))
                    sommets_vus.add((sommet1, sommet2))
        return aretes
