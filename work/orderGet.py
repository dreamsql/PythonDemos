import xml.etree.ElementTree as ET
import os

from collections import namedtuple

OrderInfo = namedtuple('OrderInfo', "id, isbuy, isopen, phase, lotBalance, instruomentId")


def get_order_attr(root):
    nodes = root.findall('.//Transaction')
    result = []
    for node in nodes:
        order_nodes = node.findall(".//Order")
        for orderNode in order_nodes:
           item = process_order_node(node, orderNode)
           if not (item is None):
               result.append(item)
    return result

def process_order_node(tranNode, orderNode):
    validPhases = set([0, 2, 255])
    getter = orderNode.get
    phase = int(getter('Phase'))
    isOpen = getter('IsOpen')
    lotBalance = float(getter('LotBalance'))
    if isOpen == 'True' and (phase in validPhases) and lotBalance > 0 :
        return OrderInfo(getter('ID'), getter('IsBuy'), getter('IsOpen'),getter('Phase'), getter('LotBalance'), tranNode.get('InstrumentID'))
    return None
        
        
        

def print_order(fileName):
    print('*' * 50)
    root = ET.parse(os.path.join( r'D:\work\test',fileName))
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
     print_order(r'account.txt')
    # print_order('account2.txt')
    # print_order('account3.txt')
    # print_order('account4.txt')
