import xml.etree.ElementTree as ET
import os


def get_order_attr(root):
	nodes = root.findall('.//Order')
	result = []
	for node in nodes:
		item = 'id = %s, code = %s ,isOpen = %s, isBuy = %s, tradePLFloat = %s, lotBalance = %s' % (node.get('ID'), node.get('Code'), node.get('IsOpen'), node.get('IsBuy'), node.get('TradePLFloat'),node.get('LotBalance'))
		result.append(item)
	return result

def print_order(fileName):
	print('*' * 50)
	root = ET.parse(os.path.join( r'D:\work\do3',fileName))
	result = get_order_attr(root)
	for item in result:
		print(item)



def get_duplicate_orders():
	path = r'D:\work\ws0308\alert.txt'
	root = ET.parse(path)
	orders = root.findall('.//Order')
	item_count = {}
	for order in orders:
		id = order.get('ID')
		if id not in item_count:
			item_count[id] = 1
		else:
			item_count[id] += 1
	
	for k, v in item_count.items():
		# if v > 1:
		print('id = %s, count = %d' % (k, v))


if __name__ == '__main__':
	get_duplicate_orders()
	# print_order('account.txt')
	# print_order('account2.txt')
	# print_order('account3.txt')
	# print_order('account4.txt')
