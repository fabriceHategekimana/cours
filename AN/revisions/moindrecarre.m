
seed= rand(3);
%a= round(seed*seed');
a= [1 1 1; 1 2 1; 1 1 1];
b= [1 0 0]';
n= length(a);
l= zeros(size(a));

for k= [1:1:n]
	l(k,k)= sqrt(a(k,k)-(l(k,1:k-1)*l(k,1:k-1)'));
	for i= [k+1:1:n]
		l(i,k)= (a(i,k)-(l(i,1:k-1)*l(k,1:k-1)'))/l(k,k);
	end
end
l
