import math
x = []
for a in range(1,500):
	
	for m in range(1,500):
	
		b = a+m
		c = a*a+b*b
		d = math.sqrt(c)
		e = int(d)
		f = math.ceil(d)
		t = 0
		n = 0
		while n<len(x):
			if e==x[n]:
				t=1
				break
			else:
				n = n+1
			
		if t==0 and e>10 and e<200 and f == e:
			x.append(e)		
print("2到200总共有",len(x),"个弦数")	
xiao=x[0]
da=x[0]
p=0		
while p<93:

	if xiao > x[p]:
		
		xiao = x[p]

	p=p+1
	
p=0
while p<93:

	if da < x[p]:
	
		da = x[p]
		
	p=p+1	
print("最大值：",da)
print ("最小值：",xiao)
