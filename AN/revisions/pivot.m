




a= [0 5 7; 5 2 5; 3 4 5];
b= [17 14 16]';
n= length(a);

for k= [1:1:n]
	%recherche du meilleur pivot
	pivot= k;
	for i= [k+1:1:n]
		if a(i,k) > a(pivot,k)
			pivot= i;
		end
	end
	%échange
	v= a(k,:); 
	a(k,:)=  a(pivot,:);
	a(pivot,:)= v;
	%on met le pivot à un en le divisant lui et sa ligne
	a(k,:)= a(k,:)/a(k,k);
	%on soutrait ce qui est en bas
	for i= [k+1:1:n]
		i
		a(i,:)= a(i,:)-(a(k,:)*a(i,k));
		a
	end
end
n
