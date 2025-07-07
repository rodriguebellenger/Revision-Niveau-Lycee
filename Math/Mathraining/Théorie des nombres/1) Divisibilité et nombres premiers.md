Si $a$ et $b$ sont des entiers positifs, on dit que $a$ est divisible par $b$, $a$ est multiple de $b$ ou que $b$ divise $a$ s'il existe un entier positif $k$ tel que $a=k\cdot b$  et on note $b\mid a$.

Un nombre premier est un nombre possédant précisément deux diviseurs (positifs) 
Puisqu'un nombre $n\in\mathbb N$ est toujours divisible par $1$ et par $n$, alors un nombre premier n'a que ces diviseurs.

Un nombre composé est un nombre qui n'est ni $1$, ni premier.

Il existe une infinité de nombre premier
Preuve : 
Supposons que nous avons une liste de tous les nombres premiers notées $p_1, p_2, p_3, \ldots, p_n$. On considère alors le nombre $q=p_1+p_2+p_3+\ldots+p_n+1$. Il n'est divisible par aucun des nombres premiers dans notre liste et n'y est pas lui-même. C'est absurde, puisque nous avions supposé que tous les nombres premiers y étaient, donc il existe une infinité de nombres premiers.

Théorème fondamental de l'arithmétique : 
Pour tous $n\in\mathbb N$, il existe d'unique nombres premiers $p_1<p_2<\ldots<p_i$ et des entiers strictement positif $e_1, e_2, \ldots, e_i$ tel que : 
$$n=p_{1}^{e_1}\cdot p_{2}^{e_2}\cdot p_{3}^{e_3}\cdot\ldots\cdot p_{i}^{e_i}$$

On peut trouver le nombre de diviseur d'un nombre grâce à ça décomposé en produit de facteur premier.
Si $n\in\mathbb N$ a pour décomposition $n=p_{1}^{e_1}\cdot p_{2}^{e_2}\cdot\ldots\cdot p_{k}^{e_k}$ alors $n$ possède exactement $(e_1+1)\cdot(e_2+1)\cdot\ldots\cdot(e_k+1)$ diviseurs positifs.

