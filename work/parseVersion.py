
# !#/usr/bin/python3

import re
import glob
import os



def parseTradingAccountVersionData(id, file):
    # pattern = 'AddNormalBalanceOnly accountId = %s' % id
    pattern = 'IncreaseVersion accountId = %s' % id
    # print(pattern)
    for line in file:
        m = re.search(pattern, line,re.IGNORECASE )
        if m:
            print(line)



def getAllFIlesAndSort(p):
    result = glob.glob(p)
    result.sort(key = sort_handle,reverse=True)
    return result

def sort_handle(filePath):
    filename = os.path.basename(filePath)
    items = filename.split('.')
    return 0 if len(items) == 2 else int(items[2])
    



if __name__  == '__main__':

    # IncreaseVersion accountId = c3ba8fd0-59fd-4e9e-8d99-2199ac10c3c7, oldVersion = 303, newVersion = 304,accountBalance = 83113.10
    # pattern = 'IncreaseVersion accountId = c3ba8fd0-59fd-4e9e-8d99-2199ac10c3c7'
    # path = 'D:\work\geg\mylogfile.txt'

    # with open(path) as f :
    #     for line in f :
    #         m = re.search(pattern, line)
    #         if m:
    #             print(line)

    files = getAllFIlesAndSort('D:\work\geg\*.txt*')
    id = '05db37a0-99c8-4124-9c1d-10a45dc3deaf'
    for file in files:
       print(file)