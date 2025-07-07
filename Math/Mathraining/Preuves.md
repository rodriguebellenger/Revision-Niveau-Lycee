#### Preuves directes : 
On veux prouver que $P\Rightarrow Q$ 
On suppose que $P$ est vrai et on fait des déduction logique à partir de là
Ex : Si $x$ et $y$ sont impair, alors $x+y$ est pair
Preuve : 
On suppose que $x$ et $y$ sont impairs. Il existe alors des entiers $k$ et $l$ tel que :
$x=2k+1$ et $y=2l+1$ 
On a alors : $x+y=2k+1+2l+1=2k+2l+2=2(k+l+1)$ 
On en conclut que $x+y$ est pair

#### Preuve par contraposition : 
$P\Rightarrow Q$ est équivalent à $\lnot P\Rightarrow \lnot Q$ et c'est donc ce que l'on va chercher à prouver
Ex : Soit $m, n\in\mathbb R$ avec $m\neq0$ et $f : \mathbb R\to\mathbb R$ la fonction définie par $f(x)=mx+n$. Montrer que si $x\neq y$, alors $f(x)\neq f(y)$ 
Preuve : 
On suppose que $f(x)=f(y)$.
Alors $mx+n=my+n$ et donc $m(x-y)=0$
Or $m\neq0$, donc $x=y$

#### Preuve par l'absurde : 
On suppose que $P$ est vrai mais que $Q$ est faux et on essaye de trouver une contradiction
Ex : Montrer que la racine carré d'un nombre premier est irrationnel
Preuve : 
On suppose que $p$ est un nombre premier et que sa racine carré est rationnel, donc $\sqrt p=\dfrac{a}{b}$ (une fraction irréductible)
On en déduit que $p=\dfrac{a²}{b²}\Leftrightarrow pb²=a²$ 
Il en suit que $a²$ est divisible par $p$, et donc $a$ aussi. On note alors $a=pa'$ avec $a'\in\mathbb Z$.
$pb²=p²a'²\Leftrightarrow b²=pa'²$ 
Par conséquent, $b²$ est divisible par $p$, et $b$ aussi. Les nombres $a$ et $b$ sont donc divisible par $p$, mais nous avions supposé que $\dfrac{a}{b}$ était irréductible. C'est donc une contradiction.