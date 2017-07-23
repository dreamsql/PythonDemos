def make_averager():
	series = []

	def averger(new_value):
		series.append(new_value)
		total = sum(series)
		return total / len(series)

	return averger	


def make_averager2():	
	total = 0
	count = 0

	def averger(new_value):
		nonlocal total, count
		total += new_value
		count += 1
		return total / count

	return averger	
