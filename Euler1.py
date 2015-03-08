

def isMultipleOf35(number):
	if number%3==0:
		return True;
	elif number%5==0:
		return True;
	else:
		return False;


def listAllValuesUpTo(max):
	list=[x for x in range(max) if isMultipleOf35(x)];
	return list;
	
val=listAllValuesUpTo(1000)
print(sum(val))
