© Nicholas Ieng Kit Ho, 2016. All rights reserved. Cannot be copied, re-used, or edited

# SAMPLE CODE

def main(k, T, filename):

	with open(filename) as f:
		text = f.read()

	kgrams = dict()
	circ_text = text + text[:k]
	for i in xrange(len(text)):
		kgram = circ_text[i:i+k]
		next_char = circ_text[i+k]
		if kgram in kgrams:
			kgrams[kgram].append(next_char)
		else:
			kgrams[kgram] = [next_char]

	current = text[:k]
	sys.stdout.write(current)
	for i in range(T-k):
		new = random.choice(kgrams[current])
		sys.stdout.write(new)
		current = current[1:]+new
	print ''
	
if __name__ == "__main__":
	k = sys.argv[1]
	T = sys.argv[2]
	filename = sys.argv[3]

	k = int(k)
	T = int(T)
	
	main(k,T,filename)

