# Euler 123


import PrimeMaestro


lots_of_primes=PrimeMaestro.getPrimesBelow(10**7)

print len(lots_of_primes)

remainder_lower_limit=25
for n in xrange(1,len(lots_of_primes)):
	left=(lots_of_primes[n]-1)**n+(lots_of_primes[n]+1)**n
	if left % (lots_of_primes[n]**2)>remainder_lower_limit:
		print "success"
		print n
		break


# (a**2+b**2)/(c**2)=root(a**2+b**2)



