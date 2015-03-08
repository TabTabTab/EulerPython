# fibo module


def primeFactorsOf(value):
	primeFactors=[];
	i=2;
	while(value!=1):
		if(value%i==0):
			value=value//i;
			primeFactors.append(i);
		else:
			i=i+1;


	return primeFactors;

def getPrimes(max):
	primes=[];
	for i in range(2,max+1):
		isPrime=True;
		for x in primes:
			if i%x==0:
				isPrime=False;
				break;
		if isPrime:
			primes.append(i);
	return primes;


