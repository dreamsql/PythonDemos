







def find(a):
	result = a[0]
	for i in range(1,len(a)):
		result ^= a[i]
	return result



if __name__ == '__main__':
	print(find([1,2,2,2,1,7]))
