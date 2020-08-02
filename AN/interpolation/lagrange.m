

function res= lagrange(A,x,y)
	L= 0;
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
		L=L+(l*y(i))
	end
	res= L;
end
