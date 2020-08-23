


%intégration avec f(x)= x; s variables; interval [0;1]

f= @(x)(cos(x));

b= [1/8 3/8 3/8 1/8];
x= linspace(0, 1, 4)
y= f(x);

res = sum(b.*y)
test= sin(1)

