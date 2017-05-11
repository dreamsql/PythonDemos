import xml.etree.ElementTree as ET
import glob
import re

def getOrderSet(orders):
	result = []
	for order in orders:
		if not 'IsOpen' in order.attrib:
			result.append(order.get('ID'))
	return result

def getOpenOrders(orderRelations):
	result = []
	for orr in orderRelations:
		result.append(orr.get('OpenOrderID'))
	return result


def getAllSortedFiles(pattern):
	repa = 'mylogfile\.txt\.?(\d+)?'
	files = glob.glob(pattern)
	files.sort(key = sort_fun,reverse=True)
	for f in files:
		print(f)

def sort_fun(f):
	repa = 'mylogfile\.txt\.?(\d+)?'
	m = re.search(repa,f.strip())
	return int(m.group(1) or 0)


if __name__ == '__main__':
	getAllSortedFiles('D:\\work\\mic\mylogfile.*')

	# tree = ET.parse('D:\\work\\mic\\account.txt')
	# orders = tree.findall('.//Order')
	# orderRelations = tree.findall('.//OrderRelation')
	# olist = getOrderSet(orders)
	# orrs = getOpenOrders(orderRelations)
	# print('balance = 0 orders count = %d' % len(olist))
	# print('openOrders count = %d' % len(orrs))
	# openOrderExcluded = 0
	# for op in orrs:
	# 	if not op in olist:
	# 		openOrderExcluded += 1
	# 		print(op)
	# print('openOrderExcluded  = %d' % openOrderExcluded )


			
