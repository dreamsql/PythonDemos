
import sys
from datetime import date
import os
import shutil


app_map = {
    'ts':'Core',
    'gw': 'Gateway',
    'ss': 'StateServer'
}

debug = 'bin\Debug'
release = 'bin\Release'


def parse_modes(args):
    modes = dict()
    for v in args:
        if v.startswith('-'):
            items = v.split('=')
            modes[items[0][1:]] = items[1]
    return modes
    


if __name__ == '__main__':
    sourceRoot = r'D:\Teams\iExchangeCollection\iExchange3 Team\iExchange3Promotion'
    targetRoot = r'D:\work\test'

    now = date.today()
    targetDir = now.strftime('%Y-%m-%d')

    modes = parse_modes(sys.argv)

    appname =app_map[modes['app']]
    
    build_type = modes['build']
    isDebug = True if build_type == 'd' or build_type == 'debug' else False

    targetDir = os.path.join(targetRoot,targetDir,appname)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir, exist_ok=True)
    
    fileDir = debug if isDebug else release
    sourceDir = os.path.join(sourceRoot, appname,fileDir)
    
    fileNames = ['Core', 'Protocal']

    # shutil.copyfile()

    for name in fileNames:
        join = os.path.join
        file1 = name + '.pdb'
        file2 = name + '.dll'
        shutil.copy2(join(sourceDir, file1), join(targetDir, file1))
        shutil.copy2(join(sourceDir, file2), join(targetDir, file2))

    print('done')
    
    
    
