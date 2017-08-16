import math
import sys





class Solution(object):
	def constructRectangle(self, area):
		mid = int(math.ceil(math.sqrt(area)))
		source = []
		source.append((area,1))
		for i in range(2,mid + 2):
			j = area / float(i)
			int_j = int(j)
			if int_j == j:
				if (i, int_j) in source: continue
				source.append((i,int_j))
				if i != int_j:
					source.append((int_j, i))
		result = []
		smallDiff = sys.maxsize
		for (length, width) in  source:
			if length < width: continue
			delta = length - width
			if smallDiff > delta: smallDiff = delta

		for (length, width) in  source:
			delta = length - width
			if delta == smallDiff:
				result.append(length)
				result.append(width)
		return result
			


		
		
        