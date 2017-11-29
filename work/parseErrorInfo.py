import re
import glob
from enum import Enum
import os

class LogLevel(Enum):
	Info = 1
	Wran = 2
	Error = 3


def filter_log_with_directory(pattern, dirPath, isReverse = False ,fileCount = None):
	files = getAllSortedFiles(dirPath, isReverse)
	count = fileCount or len(files)
	print('count = %d' % count)
	for f in files:
		count -= 1
		if count < 0: break
		filterLog(pattern,os.path.join(dirPath, f))


	
def getAllSortedFiles(pattern,isreverse):
	repa = 'mylogfile\.txt\.?(\d+)?'
	files = glob.glob(pattern)
	files.sort(key = sort_fun,reverse=isreverse)
	return files

def sort_fun(f):
	repa = 'mylogfile\.txt\.?(\d+)?'
	m = re.search(repa,f.strip())
	return int(m.group(1) or 0)


def filterLog(pattern, filePath):
	with open(filePath) as f:
		for line in f:
			if re.search(pattern, line):
				print(line)

def filter_by_tranid(tranid, filePath):
	filterLog(tranid,filePath)

def filter_by_logLevel(level, dirPath,reverse= False,filecount = None):
	if level == LogLevel.Info:
		filter_log_with_directory('INFO', dirPath, reverse,filecount)
	elif level == LogLevel.Wran:
		filter_log_with_directory('WRAN', dirPath, reverse, filecount)
	elif level == LogLevel.Error:
		filter_log_with_directory('ERROR', dirPath,reverse, filecount)





if __name__ == '__main__':
	filePath = 'D:\\work\\mic\\20170512\\mylogfile.txt'
	ws0308_path = '//ws0308/iexchange/TransactionService/Logs/mylogfile.txt'
	ws0308_dir = '//ws0308/Products/iexchange/TransactionService/Logs/mylogfile.*'
	filter_by_logLevel(LogLevel.Error,ws0308_dir)







