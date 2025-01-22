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
$$\mathbb{N}:\text{Ensemble des entiers naturels}$$
$$S(x):\text{Fonction successeur, renvoie l'entier naturel suivant}$$

Axiome de Peano :
$$\begin{gather}
\text{Axiome de l'existence du 0.}\\
0\in\mathbb{N}\\
\text{0 est un entier naturel.}\\
\\
\text{Axiome de l'égalité réflexive.}\\
\forall x\in\mathbb{N}\hspace{2mm}(x\in \mathbb{N}\rightarrow x=x)\\
\text{Tout entier naturel est égal à lui-même.}\\
\\
\text{Axiome de l'égaité symétrique}\\
\forall x\forall y\in\mathbb{N}\hspace{2mm}(x=y\rightarrow y=x)\\
\text{Pour tout entier naturel, si x égal y, alors y égal x.}\\
\\
\text{Axiome de l'égalité transitive.}\\
\forall x\forall y\forall z\in\mathbb{N}\hspace{2mm}((x=y\land y=z)\rightarrow(x=z))\\
\text{Si x égal y et y égal z, alors x égal z.}\\
\\
\text{Axiome de l'existence du successeur.}\\
\forall x\in\mathbb{N}\hspace{2mm}(x\in\mathbb{N}\rightarrow \exists S(x)\in\mathbb{N})\\
\text{Si x appartient à N, alors il existe un successeur à x appartenant à N}\\
\\
\text{Axiome de non-nullité du successeur.}\\
\forall x\in\mathbb{N}\hspace{2mm}(\neg(S(x)=0))\\
\text{0 n'est le successeur d'aucun nombre naturel.}\\
\\
\text{Axiome de l'injectivité du successeur.}\\
\forall x\forall y\in\mathbb{N}\hspace{2mm}(S(x)=S(y)\rightarrow x=y)\\
\text{Deux entier naturels distincts ne peuvent pas avoir le même successeur }\\\text{(par contraposition, si deux nombres naturels ont le même successeur, ils sont égaux.)}\\
\\
\text{Axiome de récurrence.}\\
\forall X\hspace{2mm}(0\in X\land\forall x(x\in X \rightarrow S(x)\in X)\rightarrow\forall x(x\in\mathbb{N}\rightarrow x\in X\land X=\mathbb{N}))\\
\text{Si un ensemble contient 0 et que pour tout x, si l'ensemble contient x}\\\text{ alors il contient aussi S(x), il est égal à N.}
\end{gather}$$

Axiomes d'arithmétique de Peano :
Addition :
$$\begin{gather}
\text{Axiome de simplification.}\\
\forall x\in \mathbb{N}\hspace{2mm}(x+0=x)\\
\text{Cela permet de supprimer le + opérateur et de simplifier l'équation.}\\
\\
\text{Axiome de réduction.}\\
\forall x\forall y\in \mathbb{N}\hspace{2mm}(x+S(y)=S(x+y))\\
\text{Cela permet de faire apparaître un 0, qui sera supprimer.}
\\
\end{gather}$$
Soustraction :
$$\begin{gather}
\text{Axiome de simplification.}\\
\forall x\in \mathbb{N}\hspace{2mm}(x-0=x)\\
\text{Cela permet de supprimer le - opérateur et de simplifier l'équation.}\\
\\
\text{Axiome de réduction}\\
\forall x\forall y\in \mathbb{N}\hspace{2mm}(x>=y\rightarrow x-S(y)=x-y-1)\\
\end{gather}$$

Forme rigoureuse des nombres :
Nous sommes en base 10, nous avons donc 10 symboles.
$$\begin{gather}
0=0\\
S(0)=1\\
S(S(0))=2\\
S(S(S(0)))=3\\
S(S(S(S(0))))=4\\
S(S(S(S(S(0)))))=5\\
S(S(S(S(S(S(0))))))=6\\
S(S(S(S(S(S(S(0)))))))=7\\
S(S(S(S(S(S(S(S(0))))))))=8\\
S(S(S(S(S(S(S(S(S(0)))))))))=9\\
\\
\text{Quand on atteint 9, on le remet à 0 et on remplace le chiffre d'à côté par on successeur.}\\
\text{Quand il n'y avait pas encore de nombre à côté, on concidère que c'est un 0.}\\
S(S(S(S(S(S(S(S(S(S(0))))))))))=10\\
\end{gather}$$

Preuve que 1+1=2 :
$$\definecolor{myred}{rgb}{0.6, 0, 0}$$
$$\begin{gather}
\colorbox{blue}1+\colorbox{myred}1=\colorbox{green}2\\
\colorbox{blue}{S(0)}+\colorbox{myred}{S(0)}=\colorbox{green}{S(S(0))}\\
\text{J'utilise l'axiome de réduction, avec x=\colorbox{blue}{S(0)} et y=\colorbox{myred}0.}\\
\colorbox{myred}{S(}\colorbox{blue}{S(0)}\colorbox{myred}{+0)}=\colorbox{green}{S(S(0))}\\
\text{J'utilise l'axiome de simplification afin de faire disparaître le 0.}\\
\colorbox{green}{S(S(0))}=\colorbox{green}{S(S(0))}\\
2=2\\
\text{Nous arrivons à 2=2, ce qui est vrai selon l'axiome de l'égalité réfléxive.}\\
\text{Nous pouvons donc en conclure que l'équation 1+1=2 est vrai.}
\end{gather}$$