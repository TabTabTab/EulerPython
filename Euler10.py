import PrimeMaestro




def primeSumBelow(n):
	primeList=PrimeMaestro.getPrimesBelow(n);
	return sum(primeList);

primeSum=primeSumBelow(2000000);
print primeSum;
