	
class Solution(object):

	def singleNumber(self, nums):
		result = nums[0]

		for i in range(1, len(nums)):
			result ^= nums[i]

		return result



if __name__ == '__main__':

	sol = Solution()
	result = sol.singleNumber([1, 1, 2, 2, 3])
	print(result)