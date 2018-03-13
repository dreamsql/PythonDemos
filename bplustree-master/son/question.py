
import random
import xlwt
from datetime import datetime
from datetime import timedelta
import itertools

EMPTY = '(    )'

def tenplus(ws,style):
    records = generate_plus_items()
    count = len(records)
    all_records = itertools.permutations(records)
    generate_report(all_records, count,10)
    print('done')

def ten_sub(ws, style):
    records = generate_sub_items()
    all_records = itertools.permutations(records)
    generate_sub_report(all_records, 25, 10)
    print('done')



def generate_report(all_records, records_count, page_count):
    
    page_index = 0
    begin_row = 0
    begin_col = 0
    while page_index < page_count:
        set1 = list(all_records.__next__())
        random.shuffle(set1)
        gernate_part_report(set1, begin_row, begin_col)
        begin_col += 7
        set2 = [(op2, op1) for (op1, op2) in reversed(all_records.__next__())]
        random.shuffle(set2)
        gernate_part_report(set2, begin_row, begin_col)

        page_index += 1
        begin_col = 0
        begin_row += 10 + records_count


def generate_sub_report(all_records, records_count, page_count):
    page_index = 0
    begin_row = 0
    begin_col = 0
    while page_index < page_count:
        set1 = convert_to_sub_items( all_records.__next__())
        random.shuffle(set1)
        gernate_part_report(random.sample(set1, records_count), begin_row, begin_col,True)
        begin_col += 7
        set2 =convert_to_sub_items([(op2, op1) for (op1, op2) in reversed(all_records.__next__())])
        random.shuffle(set2)
        gernate_part_report(random.sample(set2, records_count), begin_row, begin_col,True)

        page_index += 1
        begin_col = 0
        begin_row += 10 + records_count

def convert_to_sub_items(records):
    return [(op2, op1 + op2) for (op1, op2) in records]


   

def gernate_part_report(records, begin_row,begin_col, is_sub = False):
    row = begin_row
    col = begin_col
    is_first_emtpy = False

    for op1, op2 in records:
        is_first_emtpy = row % 2 == 0 if is_sub else False
        if (not is_sub) or (not is_first_emtpy): ws.write(row, col,op1,style)
        else: ws.write(row, col,EMPTY,style)
        ws.write(row, col+1,'+',style)
        if is_sub and is_first_emtpy: ws.write(row, col + 2,op1,style) 
        elif not is_sub: ws.write(row, col + 2,op2,style)
        else: ws.write(row, col + 2,EMPTY,style)
        ws.write(row, col + 3,'=',style)
        if is_sub: ws.write(row, col + 4,op2,style)
        else: ws.write(row, col + 4,EMPTY,style)
        row += 1


def generate_plus_items():
    records = set()
    begin_time = datetime.now()
    limit_time = timedelta(seconds=5)
    while datetime.now() - begin_time <= limit_time:
        op1 = random.randint(0, 10)
        op2 = random.randint(0, 10)
        result = op1 + op2
        item = (op1, op2)
        print("in proccess!")
        if (result >= 15 and result <= 20) and item not in records:
            print('{} + {} = {},{} in records'.format(op1,op2,result, len(records)))
            records.add(item)
    return records


def generate_sub_items():
    records = set()
    begin_time = datetime.now()
    limit_time = timedelta(seconds=5)
    while datetime.now() - begin_time <= limit_time:
        op1 = random.randint(0, 10)
        op2 = random.randint(0, 10)
        result = op1 + op2
        item = (op1, op2)
        print("in proccess!")
        if result < 15 and item not in records:
            print('{} + {} = {},{} in records'.format(op1,op2,result, len(records)))
            records.add(item)
    return records


if __name__ == '__main__':
    wb = xlwt.Workbook()
    
    ws = wb.add_sheet('练习')
    ezxf = xlwt.easyxf
    style = ezxf('font: bold on; align: wrap on, vert centre, horiz center')
    tenplus( ws,style)
    wb.save(r'd:\15到20以内的加法.xls')
    # ten_sub(ws, style)
    # wb.save(r'd:\15以内的加法-加数空格.xls')
