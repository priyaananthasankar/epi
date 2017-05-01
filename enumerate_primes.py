n = int(input())

#sieve of eratosthenes
#initialize a boolean array of n numbers

prime = [True] * (n+1)
p=2
primes = []

#start loop with max value of multiples
while(p*p <= n):
	#print(p*p,n)

 	#if some multiple is true
	if(prime[p] == True):
		# for each 2p,3p,4p upto pp, mark prime[i] as False as they are multiples
		for i in range(p*2,n+1,p):
			prime[i] = False
	#increment p
	p+=1

# print the ones which are true
for p in range(2,n):
	if(prime[p]):
		primes.append(p)

print(primes)	


