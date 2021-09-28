# Euclidean Algorithm or popularly known as Divison with Remainder is an efficient way of finding gcd(a,b) of integers that are very long and inefficient to calculate by factorisation.

def gcd(a,b):
	print ("\nEuclidean Divison Algorithm\n")
	while b!=0:
		t = b
		b = a % b
		print (str(a) + " = " + str(t) +"." + str(a//t) + " + " + str(b))
		a = t
		
	return a

a = input("Enter first integer: ")
b = input("Enter second integer: ")
print("\nGreatest Common Divisor: "+ str(gcd(int(a),int(b))))