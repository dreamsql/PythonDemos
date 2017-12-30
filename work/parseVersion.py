
# !#/usr/bin/python3

import re
import glob
import os
import sys



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
    

def grep(filepath, pattern, logfile):
    with open(filepath) as f :
        for line in f :
            m = re.search(pattern, line,re.IGNORECASE)
            if m:
                print(line)
                logfile.write(line)


if __name__  == '__main__':
    dirs = {
    "ws3191": r"//ws3191\Products\iExchange\TransactionService",
    "ws3193":r"//ws3193\iExchange\TransactionService",
    'ws3195':r'//ws3195\Products\iExchange\TransactionService',
    }
    server = sys.argv[1]
    files = getAllFIlesAndSort(r'%s\Logs/*.txt*' % dirs[server])
    if(len(sys.argv) < 3):
        print("please input grep pattern!")
    else:        
        id = sys.argv[2]
        print(id)
        print(len(files))
        with open("mylog.txt", 'w') as logfile:
            for file in files:
                grep(file, id,logfile)
        # # for file in files:
    #     print(file)