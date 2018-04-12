import xml.etree.ElementTree as ET
import os
import re

from collections import namedtuple

OrderInfo = namedtuple('OrderInfo', "id, isbuy, isopen, phase, lotBalance, instruomentId")

import pyodbc


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
    
def parse_reset_accounts():
    root = ET.parse(r'D:\account.txt')
    accounts = root.findall('.//Account')
    result = set()
    for account in accounts:
        id = account.get('ID')
        if id not in result:
            result.add(id)
        else:
            print('account id={} already exists'.format(id))
        parse_account_order(account)
    
def parse_account_order(account):
    result = set()
    orders = account.findall('.//Order')
    for order in orders:
        id = order.get('ID')
        if id not in result:
            result.add(id)
        else:
            print('order id = {} already exists'.format(id))


    
  
        
    




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
    #  print_order(r'account.txt')
    # print_order('account2.txt')
    # print_order('account3.txt')
    # print_order('account4.txt')
    # parse_reset_accounts()
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 10.0};'
        r'SERVER=ws3195;'
        r'DATABASE=iExchange_V3;'
        r'UID=sa;'
        r'PWD=Omni1234'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(ID), Max(ID) FROM Trading.SaveResetStatus_Xml WHERE [Time] >= '{}'".format('2018-04-11'))
    items = [item for item in cursor]
    minID = int(items[0][0])
    maxID = int(items[0][1])
    pattern = '3619771f-3c0c-4fd8-9c1b-de8c2e840891'
    while minID <= maxID:
        cursor.execute("SELECT ResetData FROM Trading.SaveResetStatus_Xml WHERE ID = '{}'".format(minID))
        for m in cursor:
            content = m[0]
            # print(content)
            if re.search(pattern, content):
                print(content)
        minID += 1
    
            
