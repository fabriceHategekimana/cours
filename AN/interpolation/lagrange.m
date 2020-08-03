

function res= lagrange(A,x)
	L= [];
	n= length(x);
	for i = [1:1:n]
		xi= x(i)
		l=1;
		for j = [1:1:n]
			if j ~= i
				xj= x(j)
				inter= ((A-x(j))/(x(i)-x(j)))
				l= l*inter;
			end
		end
		L= [L l]
	end
	res= L;
end
