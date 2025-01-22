Symbole : 
$$\neg:\text{Négation (inverse)}$$
$$\land:\text{Et}$$
$$\lor:\text{Ou}$$
$$\rightarrow:\text{Implique}$$
$$\leftrightarrow:\text{Si et seulement si}$$
$$\forall:\text{Pour tout}$$
$$\exists:\text{Il existe}$$
$$\in:\text{Appartient à}$$
$$\notin:\text{N'appartient pas à}$$

Axiome de Hilbert :
$$\begin{gather}
\text{Addition :}\\
\\
\text{Associativité de l'addition.}\\
\forall x\forall y\forall z\hspace{2mm}((x+y)+z=x+(y+z))\\
\text{L'ordre de l'addition n'a pas d'importance.}\\
\\
\text{Commutativité de l'addition.}\\
\forall x\forall y\hspace{2mm}(x+y=y+x)\\
\text{L'ordre de l'addition n'a pas d'importance.}\\
\\
\text{Existence de l'élèment neutre pour l'addition.}\\
\forall x\hspace{2mm}(x+0=x)\\
\text{Il existe un nombre neutre qui ne change pas le résultat.}\\
\\
\text{Existence de l'inverse additif.}\\
\forall x\exists y\hspace{2mm}(x+y=0)\\
\text{Pour tout nombre, il existe un nombre qui l'annule.}\\
\\
\text{Multiplication :}\\
\\
\text{Associativité de la multiplication.}\\
\forall x\forall y\forall z\hspace{2mm}((x*y)*z=x*(y*z))\\
\text{L'ordre de la multiplication n'a pas d'importance.}\\
\\
\text{Commutativité de la multiplication.}\\
\forall x\forall y\hspace{2mm}(x*y=y*x)\\
\text{L'ordre de la multiplication n'a pas d'importance.}\\
\\
\text{Existence de l'élèment neutre pour la multiplication.}\\
\forall x\hspace{2mm}(x*1=x)\\
\text{Il existe un nombre neutre qui ne change pas le résultat.}\\
\\
\text{Existence de l'inverse multiplicatif.}\\
\forall x(x\neq 0\rightarrow\exists y\hspace{2mm}(x*y=1))\\
\text{Pour tout nombre, il existe un nombre qui l'annule.}\\
\\
\text{Général :}\\
\\
\text{Distributivité.}\\
\forall x\forall y\forall z\hspace{2mm}(x*(y+z)=x*y+x*z)\\
\text{On peut développer ou factoriser les parenthèses.}\\
\\
\text{Relation d'ordre total.}\\
\forall x\forall y\hspace{2mm}(x\leq y\hspace{1mm}\lor\hspace{1mm}y\leq x)\\
\text{Les nombres sont toujours ordonnés.}\\
\\
\text{Transitivité.}\\
\forall x\forall y\forall z\hspace{2mm}(x\leq y\hspace{1mm}\land y\leq z\rightarrow x\leq z)\\
\text{L'ordre des grandeurs se conservent.}\\
\\
\text{Antisymétrie.}\\
\forall x\forall y\hspace{2mm}(x\leq y\hspace{1mm}\land y\leq x\rightarrow x=y)\\
\text{Si les affirmations "x inférieur ou égal à y" et inversement sont vrai, alors x=y.}\\
\\
\text{Relation de l'ordre avec l'addition.}\\
\forall x\forall y\forall z\hspace{2mm}(x\leq y\rightarrow x+z\leq y+z)\\
\text{Les nombres restent ordonnés, même avec l'addition.}\\
\\
\text{Relation de l'ordre avec la multiplication.}\\
\forall x\forall y\hspace{2mm}(0\leq x\hspace{1mm}\land 0\leq y\rightarrow 0\leq x*y)\\
\text{Les nombres restent ordonnés, même avec la multiplication.}\\
\\
\text{Axiome d'Archimède.}\\
\forall x\forall y\hspace{2mm}(0<x\hspace{1mm}\land0<y\rightarrow\exists z\in\mathbb{N}\hspace{2mm}(z*x>y))\\
\text{Pour toutes x et y strictement supérieur à 0, il existe un z pour lequel x*z>y.}\\
\\
\text{Axiome de la borne supérieur.}\\
\forall S\hspace{1mm}((\exists x\in S)\hspace{1mm}\land(\exists M\in\mathbb{R}\hspace{1mm}\forall x\in S(x\leq M))\rightarrow(\exists L\in\mathbb{R}\hspace{1mm}(\forall x\in S(x\leq L)\hspace{1mm}\land\forall U\in\mathbb{R}\hspace{1mm}((\forall x\in S\hspace{1mm}(x\leq U))\rightarrow L\leq U))))\\
\text{Tout ensemble non vide majoré de nombres réels admet une borne supérieure.}\\\\
\end{gather}$$
Outil :
$$\begin{gather}
\text{Fonction successeur.}\\
S(x) = x+1
\end{gather}$$
$$G = \neg\exists x\hspace{2mm}Dem(x, gSub(\ulcorner G\urcorner, G)))$$
