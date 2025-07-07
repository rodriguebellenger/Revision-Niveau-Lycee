Définition : l'aire (en unité d'aire) situé entre la courbe de la fonction, l'axe des abscisses et deux droite $x=a$ et $x=b$
On peut l'écrire $\int_{a}^{b}f(x)\,dx$ et se lit "intégrale de $a$ à $b$ de $f(x)$ $dx$"
- $a$ et $b$ sont les bornes d'intégrations
- $x$ est la variable d'intégration

On peut résoudre des intégrale visuellement si on a une fonction simple (comme une fonction affine)

On peut encadrer une fonction monotone et positive en découpant l'intervalle $[a;b]$ en $n$ sous-intervalle de longueur $l=\frac{b-a}{n}$ 
Sur un intervalle $[x;x+l]$, l'aire sous la courbe est comprise entre l'aire du rectangle $l*f(x)$ et $l*f(x+l)$ 

![[encadrement intégral avec rectangle.png|300]] 

Propriété : 
Si la fonction est négative sur $[a;b]$, alors l'aire en unité d'aire est $-\int_{a}^{b}f(x)dx$
$\int_{a}^{a}f(x)dx=0$ 
$\int_{a}^{b}f(x)dx=-\int_{b}^{a}f(x)dx$ 
$\int_{a}^{b}f(x)dx+\int_{b}^{c}f(x)dx=\int_{a}^{c}f(x)dx$ (Relation de Chasles)
$F(x)=\int_{a}^{x}f(x)\,dx\leftrightarrow F'(x)=f(x)$ ($F$ est la primitive de $f$) Preuve : [[La dérivée de l'intégrale entre a et x de f(x) est f(x)]]