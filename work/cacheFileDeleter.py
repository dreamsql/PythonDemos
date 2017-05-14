import os
from datetime import date
from datetime import timedelta




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


if __name__ == '__main__':
	create_folders('D:\\work\\test')
	