
Rappel : $CAH\hspace{2mm}SOH\hspace{2mm}TOA\hspace{2mm};\hspace{2mm}cos=\frac{Adjacent}{Hypothénuse}/sin=\frac{Opposé}{Hypothénuse}/tan=\frac{Opposé}{Adjacent}$ 

## Cercle trigonométrique

Le sens direct, positif ou trigonométrique du cercle trigonométrique est le sens inverse des aiguilles d'un montre.
Le cercle trigonométrique est un cercle tracé dans un repère orthonormé $(O,\vec{i},\vec{j})$, orienté dans le sens direct, de centre $O$ et de rayon $1$.

Cela nous permet de faire correspondre une graduation d'une droite avec celle d'un cercle.
Par exemple, si on trace la tangente au cercle au point $A$, on peut tracer dessus un point $N$, puis "enroulé" la tangente autour du cercle afin de créer le point $M$, aux même coordonnées que $N$. Cela nous permet de voir que $AN=AM$, et donc de graduer le cercle.

![[cercle trigo.png]]

Pour graduer le cercle, nous n'allons pas utiliser les degré, mais les radians, avec $rad$ égal à l'angle au centre intersectant un arc de longueur 1.
On peut aussi la définir grâce à $\pi$, en effet :
$Périmètre=2\pi r=2\pi*1=2\pi$ donc en faisant un tour complet du cercle, on parcourt en réalité $2\pi$.
En peut en conclure ce tableau de proportionnalité entre les degrés et les radians :

| Degré  | 0°     | 30°             | 45°             | 60°             | 90°             | 180°  | 360°   |
| ------ | ------ | --------------- | --------------- | --------------- | --------------- | ----- | ------ |
| Radian | $0\pi$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $2\pi$ |
Malheureusement, on peut faire correspondre plusieurs mesure à chaque point du cercle, en enroulant plusieurs fois la tangente, ou en changeant de sens. 
Dans ces cas là : $\frac{3\pi}{4}=\frac{11\pi}{4}=\frac{-5\pi}{4}$ 
Pour régler ce, on définit la mesure principale d'un angle comme étant la seule 
mesure $x\in]-\pi;\pi]$ 
Pour déplacer un angle dans cet écart, on peut ajouter ou soustraire $2\pi$ autant de fois que l'on veut. Plus généralement : si $\theta$ est un angle, $\forall k\in\mathbb{Z},\theta+k\pi$ est ce même angle.

## $sin$ et $cos$

![[sin et cos.png]]

Sur ce schéma, on peut facilement voir que le segment bleu correspond à $cos(\theta)$ et que le segment rouge correspond à $sin(\theta)$. Cela nous permet aussi d'expliquer visuellement pourquoi est-ce qu'ils oscillent entre $0$ et $-1$.

Preuve :
Point vert=$M$ ; Point bleu=$H$ ; Point rouge=$K$

On considère le triangle $OMH$
$x:=\widehat{MOH}$ 
$cos(x)=\frac{Adjacent}{Hypothénuse}=\frac{OH}{OM}=\frac{OH}{1}=OH$ 

On considère le triangle $OMK$
$y:=\widehat{MOK}$ 
$sin(y)=\frac{Opposé}{Hypothénuse}=\frac{OK}{OM}=\frac{OK}{1}=OK$ 

Propriété :
- $-1\le cos(\theta)\le 1$ et $-1\le sin(\theta)\le 1$ 
- $cos²(\theta)+sin²(\theta)=1$ 
- $cos(\theta)=cos(-\theta)$ et $sin(-\theta)=-sin(\theta)$ 
- $\forall k\in\mathbb{Z},cos(\theta)=cos(\theta+2k\pi)$ 
- $\forall k\in\mathbb{Z},sin(\theta)=sin(\theta+2k\pi)$ 
- $cos(\pi+\theta)=-cos(\theta)$ et $sin(\pi+\theta)=-sin(\theta)$ 
- $cos(\pi-\theta)=-cos(\theta)$ et $sin(\pi-\theta)=sin(\theta)$ 
- $cos(\frac{\pi}{2}+\theta)=-sin(\theta)$ et $sin(\frac{\pi}{2}+\theta)=cos(\theta)$ 
- $cos(\frac{\pi}{2}-\theta)=sin(\theta)$ et $sin(\frac{\pi}{2}-\theta)=cos(\theta)$ 

Valeurs remarquable :

| $\theta$      | $0$ | $\frac{\pi}{6}$    | $\frac{\pi}{4}$    | $\frac{\pi}{3}$    | $\frac{\pi}{2}$ | $\pi$ |
| ------------- | --- | ------------------ | ------------------ | ------------------ | --------------- | ----- |
| $cos(\theta)$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac{1}{2}$      | $0$             | $-1$  |
| $sin(\theta)$ | $0$ | $\frac{1}{2}$      | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$             | $0$   |
![[Angle trigo.png]]
## Fonction $cos$ et $sin$

Les deux ont périodes de $2\pi$, puisque après un tour complet du cercle on retourne au point de départ.
De plus, $cos$ est pair, tandis que $sin$ est impair ($cos(\theta)=cos(-\theta)$ et $sin(-\theta)=-sin(\theta)$).
On a donc besoin de n'étudier ces deux fonctions que sur l'intervalles $[0;\pi]$, puis recréer le reste de la fonction avec une symétrie (axiale pour $cos$ et centrale pour $sin$) et des translations de $2\pi$.