


variables:
i, j, tab

avant
r4= tab
r5= i
r6= j
r7= intermédiaire

bloc comment faire:

start->bloci->blocj->echa->end

start
	r4= tab
	r5=10
	r6=0
	r7=0

bloci
	i<0
	end
	i--
	j= 0
	blocj

blocj
	if j == i:
		bloci
	if t[j] < t[j+1]:
		echa
	j++

echa
	intermédiaire= t[j]
	t[j]= t[j+1]
	t[j+1]= intermédiaire
	j++
	blocj
