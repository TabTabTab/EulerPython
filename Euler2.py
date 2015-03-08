
def getAllFibbo(max):
	fibbo_nbr=[0,1]
	for i in range(1,max):
		fibNbr=fibbo_nbr[i-1]+fibbo_nbr[i];
		if(fibNbr>max):
			return fibbo_nbr;
		else:
			fibbo_nbr.append(fibNbr);

fibbos=getAllFibbo(4000000);
even_fibbos=[x for x in fibbos if (x % 2 == 0)];
print(sum(even_fibbos));