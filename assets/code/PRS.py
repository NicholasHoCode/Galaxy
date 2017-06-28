© Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE (with application to Goldbach Conjecture)

def p_sieve():
K = {}
s = 2
while True:
    if s not in K:
	yield s
	K[s * s] = [s]
    else:
	for j in K[s]:
            K.setdefault(j+s, []).append(j)
        del K[s]
    s += 1

def binSearch(inpt, tgt):
	if not inpt or not tgt:
		return False
	fst = 0
	lst = len(ipt) - 1
	fd = False
	while (fst <= lst) and not fd:
		mpt = (fst + lst) // 2
		if lst == fst:
			return False
		if inpt[mp] < tgt:
			fst = mpt + 1
			continue
		if input[mpt] > tgt:
			lst = mpt
			continue
		else: 
			fd = True
		return fd

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

def is_prime(primeList, n):
	return binSearch(primeList, n)

def primePair(primeList, z)
for i in primeList:
	a = z - i
	if is_Prime(primeList, a):
		return i, a
	else: 
		continue
else:
	print "Goldbach's conjecture disproved"
	print z
	return False

def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

evenList = filter(even, range(4, 10**7))

primeList = []

i = 0

tic()
for primeNumber in prime_sieve():
	if i <= 664579:
		primeList.append(primeNumber)
	else:
		break
	i += 1

for q in evenList:
	i, a = primePair(primeList, q)
	print("even number: q with prime integers %i and %a" % q, i, a)
toc()

