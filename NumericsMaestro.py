def product(list):
	product=1;
	for x in list:
		product*=x;
	return product;

def dictProduct(dict):
	product=1;
	for k in dict:
		product*=(k**dict[k]);
	return product;

def stringProduct(string):
	product=1;
	for c in string:
		product*=int(c);
	return product;


def digit_array(nbr):
	return map(int,str(nbr))

def is_bouncy(nbr):
	return bouncy_status(nbr)==3



# returns an int indicating the bonucy status of the argument
# potential return values:
#	0: homocreasing
#	1: increasing
#	2: decreasing
#	3: bouncy
def bouncy_status(nbr):
	nbr_array=map(int,str(nbr))
	status=0
	lastValue=nbr_array[0]
	for v in nbr_array[1:]:
		if v<lastValue:
			status = status | 2
		elif v>lastValue:
			status = status | 1
		lastValue = v
	return status


#http://en.wikipedia.org/wiki/Scientific_notation
def sci_notation_exponent(nbr):
	if nbr >0:
		return len(str(nbr))-1
	return 0




