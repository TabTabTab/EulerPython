

# a^2+b^2=c^2

def isPythagoranTriplet(a,b,c):
	return (a**2+b**2==c**2);

sum=1000;
found=False;
for c in range(sum,sum//3,-1):
	if found:
		break;
	for b in range(c-1,1,-1):
		if found:
			break;
		a=sum-c-b;
		if(a>=b or a<0):
			break;
		if(isPythagoranTriplet(a,b,c)):
			print ("a:%s b:%s c:%s product:%s" % (a,b,c,a*b*c));
			found=True;



