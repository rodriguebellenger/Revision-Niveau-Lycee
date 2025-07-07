Si $n\in\mathbb N⁰$ et $a, b\in\mathbb Z$ et que $n\mid a-b$ alors $a$ est égal à $b$ modulo $n$ ou que $a$ est congru à $b$ modulo $n$.
Cela revient à considérer leurs restes après une division euclidienne par $n$ et voir s'ils sont égaux.
On peux le noter : $a\equiv b\pmod{n}$ 

Propriété : 
Si $a\equiv b\pmod{n}$ et $c\equiv d\pmod{n}$ alors :
$a+c\equiv b+d\pmod n$ 
$a-c\equiv b-d\pmod n$ 
$ac\equiv bd\pmod n$ 

Théorème de Wilson
$(p-1)!\equiv -1\pmod{p}$   

Notion d'inverse : 
Chez les nombre réels, nous savons que tous réels non-nuls admet un inverse ($\forall x\in\mathbb R_0, \exists y\in\mathbb R_0\Rightarrow x\cdot y=1$)
Donc on dire que $y$ est l'inverse de $x$ modulo $n$ si $x\cdot y\equiv 1\pmod{n}$ 

Existence de l'inverse : $x$ possède un inverse modulo $n$ si et seulement si $(x,n)=1$
Unicité de l'inverse : si $x$ possède un inverse modulo $n$, alors cet inverse est unique modulo $n$
Pour le trouver, on applique l'algorithme d'Euclide sur $x$ et $n$, puis on utilise le théorème de Bézout. Le nombre qui multipliera $x$ sera l'inverse de $x$ modulo $n$
Ex : 
Calculons l'inverse de $13$ modulo $31$
D'abords vérifions que $(13,31)=1$
$31=2\cdot13+5$ 
$13=2\cdot5+3$
$5=1\cdot3+2$
$3=1\cdot2+1$
$2=2\cdot1+0$
Donc $(31, 13)=1$ 
Ensuite, appliquons le théorème de Bézout
$3-2=1$
$3-5+3=1$
$13-2\cdot5-5+13-2\cdot5=1$
$13-2\cdot(31-2\cdot13)-31+2\cdot13+13-2\cdot(31-2\cdot13)=1$ 
$13-2\cdot31+4\cdot13-31+2\cdot13+13-2\cdot31+4\cdot13=1$ 
$-5\cdot31+12\cdot13=1$ 
Donc $x=-5$ et $y=12$ 
Donc l'inverse de $13$ modulo $31$ est $12$
$13\cdot12\equiv1\pmod{31}$ 

Equations de la forme $ax\equiv b\pmod{n}$ :
Si $(a,n)=1$, alors il suffit de multiplier les deux côté par l'inverse de $a$ (noté $a^{-1}$)
Alors les solutions sont tous les $x$ congru à $ba^{-1}$ modulo $n$

Si $(a,n)=d\neq1$ et que $d\mid b$ alors il suffit de diviser $a$, $b$ et $n$ par $d$, ce qui redonne la situation $(a,n)=1$

Si $(a,n)=d\neq1$ et que $d\not\mid b$, alors il n'y a pas de solution

Système d'équations modulaire :
Il faut que tous les $n$ soit premiers entre eux pour pouvoir utilisé le théorème des restes chinois.
Il existe une unique solution modulo $M=n_1\cdot n_2\cdot\ldots\cdot n_i$ valant $x\equiv a_1\cdot M_1\cdot y_1+\ldots+a_i\cdot M_i\cdot y_i\pmod{M}$ 
où $a_i$ vaut les reste, $M_i$ vaut $\dfrac{M}{m_i}$ et $y_i$ est l'inverse modulaire de $M_i$ 
Ex : 
$\left\{\begin{eqnarray}x&\equiv& 5\pmod{7}\\ x&\equiv&9\pmod{11}\\ x&\equiv&11\pmod{13}\end{eqnarray}\right.$ 
D'abords, $M=7\cdot11\cdot13=1001$ 
$M_1=\dfrac{M}{m_1}=\dfrac{1001}{7}=143$ 
$M_2=\dfrac{M}{m_2}=\dfrac{1001}{11}=91$ 
$M_3=\dfrac{M}{m_3}=\dfrac{1001}{13}=77$ 
Il faut maintenant trouvé l'inverse modulaire de chacun de ces $M_i$ en utilisant la résolution d'équation linéaire
$M_1\cdot y_1\equiv1\pmod{m_1}$ donc $143\cdot y_1\equiv 1\pmod{7}$ 
$143=7\cdot20+3$; $7=3\cdot2+1$; $3=3\cdot1+0$ donc $(143,7)=1$ 
$7-3\cdot2=1$; $7-(143-7\cdot20)\cdot2=1$ donc $-143\cdot2+7\cdot41=1$ et $y_1=-2$ 

$M_2\cdot y_2\equiv1\pmod{m_2}$ donc $91\cdot y_1\equiv 1\pmod{11}$ 
$91=8\cdot11+3$; $11=3\cdot3+2$; $3=1\cdot2+1$; $2=2\cdot1+0$ donc $(11,91)=1$ 
$3-2=1$; $3-11+3\cdot3=1$; $91-8\cdot11-11+3\cdot(91-8\cdot11)=1$; $91-8\cdot11-11+3\cdot91-24\cdot11=1$ donc $4\cdot91-33\cdot11=1$ et $y_2=4$ 

$M_3\cdot y_3\equiv1\pmod{m_3}$ donc $77\cdot y_3\equiv 1\pmod{13}$ 
$77=13\cdot5+12$; $13=12\cdot1+1$; $12=12\cdot1+0$ donc $(77,13)=1$
$13-12=1$; $13-77+13\cdot5=1$ donc $-77+13\cdot6=1$ et $y_3=-1$

Pour conclure, $x=5\cdot143\cdot(-2)+9\cdot91\cdot4+11\cdot77\cdot(-1)=999$, ce qui est la solution finale