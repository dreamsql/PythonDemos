import shutil
import os



def get_all_files():
	dir = r'D:\Teams\iExchangeCollection\iExchange3 Team'
	dest_dir = r'D:\work\update'
	target = {'Core': False, 'Gateway': False, 'Protocal': False, 'StateServer': False}
	extens = ['.dll', '.pdb']
	for dirpath, dirnames, filenames in os.walk(dir):
		for each_dir in dirnames:
			if each_dir in target:
				each_dir_path = os.path.join(dirpath, each_dir)
				files = [d for d in os.listdir(each_dir_path) if os.path.isfile(os.path.join(each_dir_path, d))]
				for each_file in files:
					_, ext = os.path.splitext(os.path.join(each_dir_path, each_file))
					if ext in extens:
						print(each_file)



def is_all_visited(a):
	for k, v in a.items():
		if not v:
			return False
	return True







if __name__ == '__main__':
	get_all_files()













