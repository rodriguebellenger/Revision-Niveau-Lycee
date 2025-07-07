Primitive : si $F'(x)=f(x)$ ($f$ doit être continue) alors $F$ est une primitive de $f$ ($primitive\leftrightarrow dérivée$)

Equation différentielle : équation dont l'inconnue est une fonction et où interviennent des dérivées de cette fonction (cela revient à dire que quand on a une fonction $f$, on cherche la fonction $g$ dont la dérivée est égal cette fonction ($g'(x)=f(x)$) et est donc une primitive (on peut renommer $g$ en $F$))

Propriété : 
Toute fonction continue sur un intervalle admet des primitives sur cet intervalle
Si $F$ est une primitive de $f$, alors $G(x)=F(x)+C$ est aussi une primitive ($G-F=C$)
Si $F$ est un primitive de $f$ et $G$ est une primitive de $g$ : 
- $F+G$ est une primitive de $f+g$
- $kF$ est une primitive de $kf$ avec $k\in\mathbb R$ 

Primitives usuelles : 
$f(x)=a, a\in \mathbb{R}\leftrightarrow F(x)=ax$ 
$f(x)=x^n, n\in\mathbb{Z}-\{-1;0\}\leftrightarrow F(x)=\frac{x^{n+1}}{n+1}$ 
$f(x)=\frac{1}{x²}\leftrightarrow F(x)=-\frac{1}{x}$ 
$f(x)=\frac{1}{x}, x>0\leftrightarrow F(x)=ln(x)$ 
$f(x)=\frac{1}{\sqrt x}\leftrightarrow F(x)=2\sqrt x$ 
$f(x)=e^x\leftrightarrow F(x)=e^x$ 
$f(x)=cos(x)\leftrightarrow F(x)=sin(x)$ 
$f(x)=sin(x)\leftrightarrow F(x)=-cos(x)$  

Primitives de fonctions composées ($u$ est une fonction dérivable sur $I$ et est un raccourci pour $u(x)$) : 
$f(x)=u'u^n, n\in\mathbb{Z}-\{-1;0\}\leftrightarrow F(x)=\frac{1}{n+1}u^{n+1}$ 
$f(x)=\frac{u'}{\sqrt{u}}\leftrightarrow F(x)=2\sqrt{u}$  
$f(x)=\frac{u'}{u}, u>0\leftrightarrow F(x)=ln(u)$ 
$f(x)=u'e^u\leftrightarrow F(x)=e^u$ 
$f(x)=u'cos(u)\leftrightarrow F(x)=sin(u)$
$f(x)=u'sin(u)\leftrightarrow F(x)=-cos(u)$ 

Propriété équations différentielles :
$y'=ay, a\in\mathbb R\iff y=Ce^{ax}$ 
Si $f$ et $g$ sont solution de l'équation $y'=ay$, alors $f+g$ et $kf, k\in\mathbb R$ aussi
$y'=ay+b$ a pour solution particulière constante $f(x)=-\frac{b}{a}$  
$y'=ay+b$ a pour autres solutions $f(x)=Ce^{ax}-\frac{b}{a}$ (la solution de $y'=ay$ + la solution particulière constante de $y'=ay+b$)
$y'=ay+f$ a pour solution $f(x)=Ce^{ax}+p(x)$ avec $p(x)$ étant une solution particulière de l'équation (donnée par l'énoncé)