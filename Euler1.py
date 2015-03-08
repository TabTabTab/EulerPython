

def isMultipleOf35(number):
	if number%3==0:
		return True;
	elif number%5==0:
		return True;
	else:
		return False;


list=[x for x in range(1000) if isMultipleOf35(x)];
print(sum(list));
