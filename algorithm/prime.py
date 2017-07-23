
def is_prime(n):
	if n == 2 :
		return True
	if n == 3:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	i = 5
	w = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += w
		w = 6 -2
	return True


class Solution(object):
	def countPrimes(self, n):
		result = 0
		if n <= 2:
			return 0
		for i in range(2, n):
			if is_prime(i):
				result += 1
				if result > 1229:
					print('prime = %d' % i)
		return result		


if __name__ == '__main__':
	sol = Solution()
	print(sol.countPrimes(10000))