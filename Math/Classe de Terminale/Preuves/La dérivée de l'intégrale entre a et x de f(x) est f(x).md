On pose $f(x)$, une fonction strictement croissante.
On pose $F(x)=c$ 
On souhaite montrer que $F'(x)=f(x)$ et que donc $F(x)$ est un primitive de $f(x)$ 

On considère deux réels, $x$ et $x+h$ de l'intervalle $[a;b]$ où $h>0$ 
$\begin{align*}F(x+h)-F(x)&=\int_{a}^{x+h}f(x)\,dx-\int_{a}^{x}f(x)\,dx\\&=\int_{a}^{x+h}f(x)\,dx+\int_{x}^{a}f(x)\,dx\\&=\int_{x}^{a}f(x)\,dx+\int_{a}^{x+h}f(x)\,dx\\&=\int_{x}^{x+h}f(x)\,dx\end{align*}$ 
Ainsi : $F(x+h)-F(x)=\int_{x}^{x+h}f(x)\,dx$ 
Cette intégrale est comprise entre les rectangles d'aire $h*f(x)$ et $h*f(x+h)$ 
Comme la fonction est strictement croissante sur $[a;b]$ :
$h*f(x)<F(x+h)-F(x)<h*f(x+h)$ 
Puisque $h>0$, on a : $f(x)<\frac{F(x+h)-F(x)}{h}<f(x+h)$ 
$\lim_{h\to0}f(x)=f(x)$ 
Et comme $f(x)$ est continue sur $[a;b]$ : $\lim_{h\to0}f(x+h)=f(x)$ 
D'après le théorème des gendarmes : $\lim_{h\to0}\frac{F(x+h)-F(x)}{h}=f(x)$ 
Pour conclure : $F'(x)=\lim_{h\to0}\frac{F(x+h)-F(x)}{h}=f(x)$ 
$F(x)$ est bien une primitive de $f(x)$ 