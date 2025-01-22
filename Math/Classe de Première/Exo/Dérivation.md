Exo :

Déterminer $f'(4)$  pour $f(x)=2x^3-5x^2+3$ 

Pour cela, il faut déterminer $lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$ 
Pour ce faire, nous allons d'abords simplifier $\frac{f(a+h)-f(a)}{h}$ 

$$\begin{flalign*}
&\frac{f(a+h)-f(a)}{h}
\\&=\frac{f(4+h)-f(4)}{h}
\\&=\frac{2(4+h)³-5(4+h)²+3-(2*4³-5*4²+3)}{h}
\\&=\frac{2((4+h)(4+h)²)-5(16+8h+h²)+3-51}{h}
\\&=\frac{2((4+h)(16+8h+h²))-80-40h-5h²-48}{h}
\\&=\frac{2(64+32h+4h²+16h+8h²+h³)-40h-5h²-128}{h}
\\&=\frac{128+64h+8h²+32h+16h²+2h³-40h-5h²-128}{h}
\\&=\frac{64h+8h²+32h+16h²+2h³-40h-5h²}{h}
\\&=\frac{24h+3h²+32h+16h²+2h³}{h}
\\&=\frac{h(24+3h+32+16h+2h²)}{h}
\\&=24+3h+32+16h+2h²
\\&=lim_{h\to 0}24+3h+32+16h+2h²=24+32=56
\end{flalign*}$$

Formule général :

$$\begin{flalign*}
&\frac{f(a+h)-f(a)}{h}
\\&=\frac{2(a+h)³-5(a+h)²+3-(2a³-5a²+3)}{h}
\\&=\frac{2(a+h)³-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2((a+h)(a+h)²)-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2((a+h)(a²+2ha+h²))-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2(a³+2ha²+ah²+ha²+2ah²+h³)-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2a³+4ha²+2ah²+2ha²+4ah²+2h³-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2a³+6ha²+6ah²+2h³-5(a+h)²+3-2a³+5a²-3}{h}
\\&=\frac{2a³+6ha²+6ah²+2h³-5(a²+2ah+h²)+3-2a³+5a²-3}{h}
\\&=\frac{2a³+6ha²+6ah²+2h³-5a²-10ah-5h²+3-2a³+5a²-3}{h}
\\&=\frac{6ha²+6ah²+2h³-10ah-5h²}{h}
\\&=\frac{h(6a²+6ah+2h²-10a-5h)}{h}
\\&=6a²+6ah+2h²-10a-5h
\\
\\&\text{Nous pouvons maintenant replacer la limite : }
\\
\\&=lim_{h\to 0}6a²+6ah+2h²-10a-5h
\\&=6a²-10a
\\
\\&\text{Nous pouvons maintenant calculer }f'(4)
\\
\\&f'(4)=6*4²-10*4=56
\end{flalign*}$$

Exo : 

$f(x)=x²+5x+1$ 

1) Equation de la tangente au point d'abscysse $a=0$ 
Premièrement : 
$f(a)=f(0)=0²+5*0+1=1$

Deuxiémement : 
L'équation dérivée de $x²$ est $2x$
L'équation dérivée de $5x+1$ est $5$
Donc : 
$f'(x)=2x+5$
$f'(a)=f'(0)=2*0+5=5$

Or nous voulons trouver l'équation de la tangente de $f$ pour $a=0$
Donc : 
$y=f'(a)*(x-a)+f(a)=5(x-0)+1=5x+1$

2) Equation de la tangente au point d'abscysse $a=-1$
Premièrement : 
$f(a)=f(-1)=-1²+5*(-1)+1=-3$

Nous savons déjà que :
$f'(x)=2x+5$
Donc : 
$f'(a)=f'(-1)=2*(-1)+5=3$

Or nous voulons trouver l'équation de la tangente de $f$ pour $a=0$
Donc : 
$y=f'(a)*(x-a)+f(a)=3(x+1)-3=3x+3-3=3x$ 

Exo 26 p 119

$f(x)=x^3+x^2;I=\mathbb{R}$ 
$f(x)=3x^2+2x;I=\mathbb{R}$ 

$f(x)=x^3-x^2-x-1;I=\mathbb{R}$ 
$f(x)=3x^2-2x-1;I=\mathbb{R}$ 

$f(x)=\sqrt{x}+x;I=[0;+\infty[$ 
$f(x)=\frac{1}{2\sqrt{x}}+1;I=[0;+\infty[$ 

$f(x)=x²-\frac{1}{x};I=\mathbb{R}^*$ 
$f(x)=2x-\frac{-1}{x²};I=\mathbb{R}^*$ 

Exo 27 p 119

$f(x)=3x^2-4x+3;I=\mathbb{R}$ 
$f(x)=6x-4;I=\mathbb{R}$ 

$f(x)=-4x^4+3x^3-2x^2+x;I=\mathbb{R}$ 
$f(x)=-16x^3+9x^2-4x+1;I=\mathbb{R}$ 

$f(x)=x^3-2x^2-3x-4;I=\mathbb{R}$ 
$f(x)=3x^2-4x-3;I=\mathbb{R}$ 

Exo 29 p 119

$f(x)=\frac{x+1}{x-2};I=\mathbb{R}/{2}$ 
Nous savons que :
$(\frac{u}{v})'=\frac{u'v-uv'}{v^2}$
Donc : 
$\frac{x+1}{x-2}=\frac{1(x-2)-1(x+1)}{(x-2)^2}=\frac{x-2-x+1}{(x-2)^2}=\frac{-1}{(x-2)^2}$

$f(x)=\frac{x^3+1}{x^2-1};I=\mathbb{R}/{-1;1}$ 
$\frac{x^3+1}{x^2-1}=\frac{3x^2(x^2-1)-2x(x^3+1)}{(x^2-1)^2}=\frac{3x^4-3x^2-2x^4+2x}{(x^2-1)^2}=\frac{x^2-2x^4+2x}{(x^2-1)^2}$ 

$f(x)=\frac{\sqrt{x}}{x-1};I=]1;+\infty[$ 
$\frac{\sqrt{x}}{x-1}=\frac{{\frac{1}{2\sqrt{x}}}(x-1)-\sqrt{x}}{(x-1)²}$ 

$f(x)=\frac{x²+x+1}{\sqrt{x}};I=[0;+\infty[$ 

Exo 44 p 121

1) Je vois graphiquement que $f'(0)=-2$
2) Je vois graphiquement que $f'(3)=4$

Exo 66 p 124

$f(x)=-x²+4$
$g(x)=x²-4x+6$
$A(1;3)$

1) Par les propriétés et les formules du cours :
$f'(x)=-2x$
$g'(x)=2x-4$

Je vais calculer l'équation des tangentes des courbes $C_f$ et $C_g$, si elle sont égal, alors les tangentes sont les mêmes :
Pour $f$ :
$y=f'(a)*(x-a)+f(a)=(-2*1)*(x-1)-1²+4=-2(x-1)+5=-2x+7$
Pour $g$ :
$y=f'(a)*(x-a)+f(a)=(2*1-4)*(x-1)+1²-4*1+6=-2(x-1)+3=-2x+5$ 

Eval test :

Exo 1
Réponse C
Réponse D
Réponse C
Réponse D
Réponse A

Exo 2
1) $f(x)=\frac{3}{4}x^4-6x²+7$ dérivable sur $\mathbb{R}$
$f'(x)=3x^3-12x$ 

2) $f(x)=\frac{1}{x²+2x-3}$ dérivable sur $\mathbb{}$
Nous savons que : $(\frac{u}{v})'=\frac{u'v-uv'}{v²}$
$f'(x)=\frac{0(x²+2x-3)-1(2x+2)}{(x²+2x-3)²}=\frac{-2x-2}{(x²+2x-3)²}$ 

3) $f(x)=\frac{5x-3}{2x-7}$
$f'(x)=\frac{5(2x-7)-2(5x-3)}{(2x-7)²}=\frac{10x-35-10x+6}{(2x-7)²}=\frac{-29}{(2x-7)²}$ 

4) $f(x)=\frac{x²+x+1}{x-1}$
$f'(x)=\frac{(x-1)(2x+1)-(x²+x+1)}{(x-1)²}=\frac{2x²+x-2x-1-x²-x-1)}{(x-1)²}=\frac{x²-2x-2)}{(x-1)²}$ 

5) $f(x)=(x²+1)(x³-2x)$
Nous savons que : $(uv)'=u'v+uv'$
$f'(x)=2x(x^3-2x)+(3x²-2)(x²+1)=2x^4-4x²+3x^4+3x²-2x²-2=5x^4-3x²-2$

6) $f(x)=\frac{x²}{x²-2x+2}$
$f'(x)=\frac{2x(x²-2x+2)-x²(2x-2)}{(x²-2x+2)²}=\frac{2x^3-4x²+4x-2x^3+2x²}{(x²-2x+2)²}=\frac{-2x²+4x}{(x²-2x+2)²}$ 

Exo 3

$f(x)=-\frac{1}{4}x^4+2x²+1$ 
1) La fonction a l'air d'être paire, cela implique que $f(x)=f(-x)$
2) $f'(x)=-x^3+4x=x(4-x²)=x(2-x)(2+x)$
3) $x(-x²+4)=0$
$S=\{-2;0;2\}$ 

| $x$       |     |     |     |
| --------- | --- | --- | --- |
| $x$       |     |     |     |
| $4-x²$    |     |     |     |
| $x(4-x²)$ |     |     |     |
On remplie les signes en fonctions de x pour chaque équations, puis on multiplie l'une par l'autre pour le résultat de l'équation finale

4) $y=f'(a)*(x-a)+f(a)$
$f'(1)=1(2-1)(2+1)=3$
$f(1)=-\frac{1}{4}*1^4+2*1²+1=-\frac{1}{4}+2+1=2.75$

$y=3(x-1)+2.75=3x-3+2.75=3x-0.25$

Exo 4

