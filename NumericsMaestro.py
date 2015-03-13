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