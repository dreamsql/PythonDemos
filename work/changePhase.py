

def toSql(id,f):
	f.write("Update Trading.[Order]  set Phase = 3 where ID = '%s'\n" % id)
	# f.write("Update dbo.[Order]  set Phase = 3 where ID = '%s'\n" % id)


wf = open('result.txt', 'w')
with open('closeOrders.txt') as f:
	for line in f:
		toSql(line.strip('\n'),wf)
wf.close()

print('done')