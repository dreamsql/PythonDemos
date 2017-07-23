



def get(a):
	s = set()
	for i in a:
		if i not in s:
			s.add(i)
		else:
			return i
	return None

def get_missing_item_from_sorted_array(a):
	if a[0] != 0:
		return 0
	else:
		for i, v in enumerate(a):
			j = i + 1
			if j < len(a) :
				diff = a[j] - a[i]
				if diff != 1:
					return a[i] + 1
		return None

if __name__ == '__main__':
	print(get_missing_item_from_sorted_array([1, 2, 5, 6]))
	print(get_missing_item_from_sorted_array([0,1, 2, 5, 6]))
