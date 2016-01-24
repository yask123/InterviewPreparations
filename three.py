ls = [-1, -2, 1, 3, 2]
maxx = ls[0]*ls[1]*ls[2]

for i in range(len(ls)-2):
	prod=1
	for j in range(i,i+3):
		prod*=ls[j]
	if maxx < prod:
		maxx = prod

print maxx			