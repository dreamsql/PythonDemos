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



if __name__ == '__main__':
	print_order('account.txt')
	print_order('account2.txt')
	print_order('account3.txt')
	print_order('account4.txt')
