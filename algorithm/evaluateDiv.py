
from collections import deque

class Solution(object):
	def calcEquation(self, equations, values, queries):
       
		q = deque()
		result = [-1 for i in range(len(queries))]
		graph = dict()

		for i in range(len(equations)):
			item = equations[i]
			b = item[0]
			e = item[1]
			if b not in graph:
				graph[b] = []
			if e not in graph:
				graph[e] = []

			graph[b].append((e, values[i]))
			graph[e].append((b, 1.0 / values[i]))
		
		visited = set()

		for i in range(len(queries)):
			item = queries[i]
			b = item[0]
			e = item[1]
			visited.clear()
			founded = False
			if b in graph:
				q.append((b, 1.0))
				visited.add(b)

				while len(q) > 0:
					(cur, ratio) = q.pop()
					if cur == e:
						result[i] = ratio
						founded = True
						break
					adjs = graph[cur]
					for (v, r) in adjs:
						if v not in visited:
							q.append((v, ratio * r))
							visited.add(v)
			if not founded:
				result[i] = -1


		return result


if __name__ == '__main__':
	sol = Solution()
	queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a','a'], ['x', 'x']]
	result = sol.calcEquation([['a','b'], ['b', 'c']], [2.0, 3.0], queries)
	for item in result:
		print(item)

						
						



				


