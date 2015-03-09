def isPalindromeString(candidate):
	length=len(candidate);
	if(length%2!=0):
		return False;
	else:
		half=length//2;
		return candidate[:half]==candidate[half:][::-1];

