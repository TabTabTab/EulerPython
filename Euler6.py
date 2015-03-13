squareSum=0;
naturalSum=0;
for i in range(1,101):
	squareSum+=(i**2);
	naturalSum+=i;
square=naturalSum**2;
print(square-squareSum);