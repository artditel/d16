
def is_prime (n):
	k = n
	b = 2
	while k > b:
		if n % b == 0:
			return False
		else:
			k = n//b
		b = b + 1
	return True

def test_is_prime ():
	if is_prime (4) == True:
		return False
	if is_prime (13) == False:
		return False
	if is_prime (2) == False:
		return False
	if is_prime (216) == True:
		return False
	if is_prime (49) == True:
		return False
	if is_prime (11) == False:
		return False
	return True
	
