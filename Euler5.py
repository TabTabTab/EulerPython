import PrimeMaestro
import NumericsMaestro


def concatonatePrimeDicts(dict1,dict2):
	for v in dict2:
		if v in dict1:
			dict1[v]=max(dict1[v],dict2[v]);
		else:
			dict1[v]=dict2[v];
	return dict1;




factorDict={};
for v in range(1,21):
	tempDict=PrimeMaestro.primeFactorDict(v);
	factorDict=concatonatePrimeDicts(factorDict,tempDict);
print(NumericsMaestro.dictProduct(factorDict));


