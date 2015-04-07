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

def primeFactorDict(value):
	primeList=primeFactorsOf(value);
	primeDict={};
	for p in primeList:
		if p in primeDict:
			primeDict[p]+=1;
		else:
			primeDict[p]=1;
	return primeDict;

def primeFactorDictUsingPrimeList(value,primeList):
	primeDict={};
	for p in primeList:
		if p in primeDict:
			primeDict[p]+=1;
		else:
			primeDict[p]=1;
	return primeDict;


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



def getPrimesBelow(n):
	hasPotential=[True]*n;
	for i in xrange(3,int(n**0.5)+1,2):
		if(hasPotential[i]):
			fromIndex=i*i;
			stepSize=i*2;
			listLength=(n-1-fromIndex)/stepSize+1;
			hasPotential[fromIndex::stepSize]=[False]*listLength;
	return [2] + [i for i in xrange(3,n,2) if hasPotential[i]];

def getXFirstPrimes(amount):
	primes=[];
	i=1;
	while(len(primes)<amount):
		i+=1;
		isPrime=True;
		for x in primes:
			if i%x==0:
				isPrime=False;
				break;
		if isPrime:
			primes.append(i);
	return primes;
