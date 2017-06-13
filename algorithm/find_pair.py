

def findPair(a , sum):
	for i in range(len(a)):
		for j in range(i + 1, len(a)):
			if a[i] + a[j] == sum:
				print('find pair: (%d, %d)' % (a[i], a[j]))

def findPair2(a, sum):
	a.sort()
	low = 0
	high = len(a) - 1
	while low < high:
		if a[low] + a[high] == sum:
			print('find pair: (%d, %d)' % (a[low] , a[high]))
			return
		elif low + high > sum:
			high -= 1
		else: 
			low += 1
	print('not found pair: (%d, %d)' % (low , high))


def findPair3(a, sum):
	m = set()
	for i in range(len(a)):
		if  (sum - a[i]) in m: 
			print('find pair: (%d, %d)' % (a[i] , sum - a[i]))
			break;
		else:
			m.add(a[i])
	
	



if __name__ == '__main__':
	a = [8, 7, 2, 5, 3, 1]
	findPair3(a, 10)
