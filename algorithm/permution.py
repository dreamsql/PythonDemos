
def do_permution(a):
	permution_helper(a, 0)


def permution_helper(a, i):
	if i == len(a) - 1: 
		print(a)
		return
	for j in range(i, len(a)):
		swap(a,i,j)
		permution_helper(a, i + 1)
		swap(a, i, j)


def swap(a, i, j):
	temp = a[i]
	a[i]= a[j]
	a[j] = temp





if __name__ == '__main__':
	do_permution(['a', 'b', 'c', 'd'])

