Le plus grand diviseur commun (PGCD) de deux nombres naturels $x$ et $y$ est le plus grand nombre entier divisant $x$ et $y$.
Le plus petit multiple commun (PPCM) de deux nombres naturels $x$ et $y$ est le plus petit nombre entier multiple de $x$ et $y$.
Pour les trouver, on prend respectivement le minimum des puissances de chaque nombre premier de leur décomposition, ou le maximum.
$15=2⁰\cdot3¹\cdot5¹$
$20=2²\cdot3⁰\cdot5¹$
$(15,20)=2^{\min(0,2)}\cdot3^{\min(1,0)}\cdot5^{\min(1,1)}=2^0\cdot3^0\cdot5^1=5$ 
$[15,20]=2^{\max(0,2)}\cdot3^{\max(1,0)}\cdot5^{\max(1,1)}=2^2\cdot3^1\cdot5^1=60$ 

Si $x, y\in\mathbb N$, alors $(x,y)\cdot[x,y]=x\cdot y$ 

Algorithme d'Euclide : 
Tout d'abords : $(a,b)=(a-b,b)$ si $a\ge b\ge0 \,\,\,(a,b\in\mathbb N)$   
On peut l'appliquer $k$ fois avec : $(a,b)=(a-k\cdot b, b)$ tant que $a-k\cdot b\ge0$  
Ex : 
$31=2\cdot13+5$ 
$13=2\cdot5+3$
$5=1\cdot3+2$
$3=1\cdot2+1$
$2=2\cdot1+0$
Donc $(31, 13)=1$ 

Théorème de Bézout :
Soient $a, b\in\mathbb N_0$ et $c\in\mathbb Z$, il existe des entiers $x, y\in\mathbb Z$ tel que :
$ax+by=c$
si et seulement si $c$ est un multiple de $(a,b)$ 
Pour trouver $x$ et $y$, il suffit de reprendre l'algorithme d'Euclide utilisé pour trouver le PGCD et de partir de la fin en remontant.
Ex : 
On veux connaître $x, y$ tel que $31x+13y=1$ (on réutilise les calculs effectués dans l'exemple précédent)
$3-2=1$
$3-5+3=1$
$13-2\cdot5-5+13-2\cdot5=1$
$13-2\cdot(31-2\cdot13)-31+2\cdot13+13-2\cdot(31-2\cdot13)=1$ 
$13-2\cdot31+4\cdot13-31+2\cdot13+13-2\cdot31+4\cdot13=1$ 
$-5\cdot31+12\cdot13=1$ 
Donc $x=-5$ et $y=12$ 

Théorème de Gauss : 
Soient $a, b, c\in\mathbb N_0$, si $(a, c)=1$ et $c\mid ab$ alors $c\mid b$ 