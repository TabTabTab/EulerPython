#Euler112.py
import NumericsMaestro

def nextSizeNonBouncy(nonBouncyNbr):
	exponent=NumericsMaestro.sci_notation_exponent(nonBouncyNbr)+1
	nonBouncies=set()
	for i in xrange(10**exponent,10**(exponent+1),10**exponent):
		headAdded=nonBouncyNbr+i
		if not NumericsMaestro.is_bouncy(headAdded):
			nonBouncies.add(headAdded)

	for i in xrange(0,9):
		tailAdded=nonBouncyNbr*10+i
		if not NumericsMaestro.is_bouncy(tailAdded):
			nonBouncies.add(tailAdded)
	return nonBouncies

nDigitNonBouncy=set([1,2,3,4,5,6,7,8,9])
required_quota=0.99
nbrOfNumbers=9
nbrOfBouncys=0
value_found=False
while(not value_found):
	nextNDigitNonBouncy=set()
	for nonB in nDigitNonBouncy:
		newNonBouncySet=nextSizeNonBouncy(nonB)
		nextNDigitNonBouncy.update(newNonBouncySet)
	fromVal=nbrOfNumbers+1
	toVal=10*(nbrOfNumbers+1)
	for val in xrange(fromVal,toVal,1):
		nbrOfNumbers=nbrOfNumbers+1
		if val not in nextNDigitNonBouncy:
			nbrOfBouncys=nbrOfBouncys+1
			quota=nbrOfBouncys/float(nbrOfNumbers)
			if(quota>=required_quota):
				print val
				value_found=True
				break;
	nDigitNonBouncy=nextNDigitNonBouncy












