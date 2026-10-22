# Joli Algorithmes - Compte rendu des différents algorithmes

L'objectif des algorithmes et de déterminer l'enveloppe convexe de points d'un plan

### Algorithme naïf 
```naive_algorithm()```

Facile à coder: la partie pour vérifier si un point se trouve à droite ou à gauche d'un segment n'est pas compliqué. On identifie donc facilement les arrêtes. Néanmoins, on teste toutes les arrêtes, on à donc une complexité en *O(n^3)*

### Diviser pour reigner
```divide_and_conquer()```

Le plus difficile que j'ai eu à coder. La fonction fusionner m'a vraiment donné du fil a retordre. Néanmoins c'est l'un des plus rapides avec une complexités en *O(n x log(n))*.

J'ai utilisé l'algorithmes naïf pour calculer les cas de base (en dessous de 5 points), plutôt que de recopier une fonction déja existante dans le code

### Jarvis
```jarvis()```

Pas trop compliqué a coder, la complexité dépend du nombre *h* de sommets de l'enveloppe en *O(n x h)*

### Sklansky
```sklansky()```

Idem, pas aussi compliqué que diviser pour reigner. Le points faible de cet algorithme et qu'il fonctionne uniquement pour des polygones. Néanmoins, sa compléxité est en *O(n)*.

## Conclusion

L'algorithme naïf reste la méthode à absolument éviter de part sa complexité importante.

Diviser pour reigner est l'algorithme le plus polyvalents, et qui à la meilleur complexité en général. 

Dans les cas de points très concentré avec quelque points épars du centre, l'agorithme de Jarvis va être très efficace.

Enfin, l'algorithme de Sklansky est d'une très bonne compléxité, mais ne parche malheuresment que sur des points formant un polygone.
