import os
import re
from datetime import datetime
from datetime import date
from datetime import timedelta
import shutil
import sys




def create_folders(rootDir):
	now = date.today()
	target = now - timedelta(days = 10)
	while target <= now:
		subDir = target.strftime('%Y-%m-%d')
		sub_dir_path = os.path.join(rootDir, subDir)
		print(sub_dir_path)
		if not os.path.exists(sub_dir_path):
			os.makedirs(sub_dir_path)
		target += timedelta(days = 1)


def delete_folders(rootdir):
	now =date.today()
	td = timedelta(days = 7)
	pattern = '.*(20\d{2}\-\d{2}\-\d{2})$'
	fmt = '%Y-%m-%d'
	dirs = [ dir for dir in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, dir))]
	for dir in dirs:
		m =re.search(pattern, dir)
		if m and m.group(1):
			targetDatetime = datetime.strptime(m.group(1), fmt)
			targetDate = targetDatetime.date()
			if targetDate + td <= now:
				shutil.rmtree(os.path.join(rootdir, dir))
				print('%s removed' %dir)
				



if __name__ == '__main__':
	dir  = sys.argv[1]
	delete_folders(dir)
	