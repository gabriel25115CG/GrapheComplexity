from typing import List, Tuple

class GrapheNonOriente:
    def __init__(self):
        """Initialise un graphe non orienté vide utilisant une liste d'adjacence."""
        self.adjacence = {}  # Dictionnaire où chaque sommet est une clé et ses voisins sont stockés sous forme de dictionnaire.

    def ajouter_sommet(self, sommet: int) -> None:
        """Ajoute un nouveau sommet au graphe s'il n'existe pas encore."""
        if sommet not in self.adjacence:
            self.adjacence[sommet] = {}  # Initialise une entrée vide pour le sommet.

    def ajouter_arete(self, sommet1: int, sommet2: int, poids: float) -> None:
        """
        Ajoute une arête entre deux sommets avec un poids donné.
        Comme le graphe est non orienté, l'arête est ajoutée dans les deux sens.
        """
        self.ajouter_sommet(sommet1)  # S'assure que le premier sommet existe.
        self.ajouter_sommet(sommet2)  # S'assure que le second sommet existe.
        self.adjacence[sommet1][sommet2] = poids  # Ajoute l'arête de sommet1 vers sommet2.
        self.adjacence[sommet2][sommet1] = poids  # Ajoute l'arête de sommet2 vers sommet1.

    def supprimer_sommet(self, sommet: int) -> None:
        """
        Supprime un sommet et toutes ses arêtes associées.
        Cela signifie que tous les voisins du sommet doivent aussi être mis à jour.
        """
        if sommet in self.adjacence:
            # Supprime l'entrée de ce sommet dans la liste d'adjacence de ses voisins.
            for voisin in list(self.adjacence[sommet].keys()):
                del self.adjacence[voisin][sommet]
            del self.adjacence[sommet]  # Supprime le sommet du graphe.

    def supprimer_arete(self, sommet1: int, sommet2: int) -> None:
        """Supprime l'arête entre deux sommets s'ils existent et sont connectés."""
        if sommet1 in self.adjacence and sommet2 in self.adjacence:
            if sommet2 in self.adjacence[sommet1]:  # Vérifie si l'arête existe.
                del self.adjacence[sommet1][sommet2]  # Supprime dans un sens.
                del self.adjacence[sommet2][sommet1]  # Supprime dans l'autre sens.

    def obtenir_sommets(self) -> List[int]:
        """Retourne la liste de tous les sommets du graphe."""
        return list(self.adjacence.keys())

    def obtenir_aretes(self) -> List[Tuple[int, int, float]]:
        """
        Retourne la liste des arêtes sous la forme (sommet1, sommet2, poids).
        On évite les doublons en s'assurant de ne compter qu'une fois chaque arête.
        """
        aretes = []
        sommets_vus = set()  # Ensemble pour éviter de compter deux fois la même arête.
        for sommet1 in self.adjacence:
            for sommet2, poids in self.adjacence[sommet1].items():
                if (sommet2, sommet1) not in sommets_vus:  # Vérifie si l'arête a déjà été ajoutée.
                    aretes.append((sommet1, sommet2, poids))
                    sommets_vus.add((sommet1, sommet2))  # Ajoute à l'ensemble pour éviter les doublons.
        return aretes

    def obtenir_liste_adjacence(self) -> List[Tuple[int, List[Tuple[int, float]]]]:
        """
        Retourne la liste d'adjacence sous une forme lisible :
        [(sommet, [(voisin1, poids1), (voisin2, poids2), ...]), ...]
        """
        return [(sommet, list(voisins.items())) for sommet, voisins in self.adjacence.items()]
