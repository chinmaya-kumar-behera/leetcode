l = [-1,0,1,2,-1,-4]

l.sort()
ans = set()

for ind1 in range(len(l)-1):
	num1 = l[ind1]
	ind2 = ind1+1
	ind3 = len(l)-1
	while ind2 < ind3:
		num2 = l[ind2]
		num3 = l[ind3]
		trip = num1+num2+num3
		if trip == 0:
			ans.add((num1,num2,num3))
			ind2 += 1
			ind3 -= 1
		elif trip > 0:
			ind3 -= 1
		else:
			ind2 += 1
			
print(list(map(list,ans)))