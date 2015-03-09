import PalindromeMaestro
def largestProductPalind():
	a=999;
	b=999;
	largestPalindrome=0;
	for i in range(a,100,-1):
		for j in range(b,100,-1):
			product=i*j;
			if product <= largestPalindrome:
				break;
			if PalindromeMaestro.isPalindromeString(str(product)):
				largestPalindrome=product;
				break;
	return largestPalindrome;

print(largestProductPalind());
