import xlwt

from datetime import datetime


wb = xlwt.Workbook()
ws = wb.add_sheet('A test sheet')
ws.write(1,0, datetime.now())
wb.save(r'd:\mydemo.xls')