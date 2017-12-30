
import sys
from datetime import date
import os
import shutil


app_map = {
    'ts':'TransactionService',
    'gw': 'Gateway',
    'ss': 'StateServer'
}

debug = 'bin\Debug'



if __name__ == '__main__':
    source_root = r'D:\Teams\iExchangeCollection\iExchange3 Team\iExchange3Promotion'
    target_root = r'D:\work\test'
    if len(sys.argv) < 2:
        raise ValueError('should input app name')
    
    now = date.today()
    target_dir = now.strftime('%Y-%m-%d')

    appname =app_map[sys.argv[1]]

    target_dir = os.path.join(target_root,target_dir,appname)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    
    source_dir = os.path.join(source_root, appname,debug)
    
    file_names = ['Core', 'Protocal']

    # shutil.copyfile()

    for name in file_names:
        join = os.path.join
        file1 = name + '.pdb'
        file2 = name + '.dll'
        shutil.copy2(join(source_dir, file1), join(target_dir, file1))
        shutil.copy2(join(source_dir, file2), join(target_dir, file2))

    print('done')
    
    
    
