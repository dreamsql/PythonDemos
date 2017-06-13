
from operator import itemgetter



def merge(a):
	a.sort(key = lambda m : itemgetter(0)(m))
	stack = []
	for item in a:
		if len(stack) == 0 or item[0] > stack[-1][1] :
			stack.append(item)
		if stack[-1][1] <  item[1] :
			stack[-1][1] = item[1] 
		
	for item in stack:
		print(item)



if __name__ == '__main__':
	a = [[2, 3], [7,8], [12, 15], [1, 5], [4, 6], [8, 10]]
	merge(a)

