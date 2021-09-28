# Euclidean Algorithm or popularly known as Divison with Remainder is an efficient way of finding gcd(a,b) of integers that are very long and inefficient to calculate by factorisation.

def gcd(a,b):
	while b!=0:
		t = b
		b = a % b
		print (str(a) + " = " + str(t) +"." + str(a//t) + " + " + str(b)+"\n")
		a = t
		
	return a

print("Greatest Common Divisor: "+ str(gcd(2024,748)))