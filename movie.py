movies =[4,2,23,432,1,7,3]

k = 25

b=[]

for each in movies:
	if each < k:
		b.append(each)
print b
b.sort()

for each in range(len(b)-1):
	if b[each]+b[each]+1 == k:
		print b[each],b[each]+1