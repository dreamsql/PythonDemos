

def selectActivity(vc):
	k = 0
	out = set()
	out.add(0)
	for i in range(1, len(vc)):
		si, fi = vc[i]
		sk, fk = vc[k]
		if si >= fk:
			out.add(i)
			k = i
	return out

if __name__ == '__main__':

	a = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

	a.sort(key = lambda m : m[1])

	result = selectActivity(a)

	for i in result:
		print('(%s, %s)' % a[i])

		