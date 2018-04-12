
import sys
from datetime import date
import os
import shutil


class AppInfo:
    
    def __init__(self, name, fileNames):
        self.name = name
        self.fileNames = fileNames        

app_map = {
    'ts':AppInfo('Core', ['Core', 'Protocal']),
    'gw': AppInfo('Gateway', ['Gateway', 'Protocal']),
    'ss': AppInfo('StateServer', [])
}

debug = 'bin\Debug'
release = 'bin\Release'




def parse_modes(args):
    modes = dict()
    for v in args:
        print(v)
        if v.startswith('-'):
            items = v.split('=')
            modes[items[0][1:]] = items[1]
    if 'build' not in modes:
        modes['build'] = 'r'
    return modes

def get_appname_and_filedir():
    modes = parse_modes(sys.argv)
    appinfo =app_map[modes['app']]
    build_type = modes['build']
    isDebug = True if build_type == 'd' or build_type == 'debug' else False
    fileDir = debug if isDebug else release
    return (appinfo, fileDir)

def copy():
    
    sourceRoot = r'D:\work\versions\Current'
    targetRoot = r'Z:\Common\SwapFiles\Robert\NewVersionUpdate\Test'

    now = date.today()
    targetDir = now.strftime('%Y-%m-%d')
    appinfo, fileDir = get_appname_and_filedir()
    targetDir = os.path.join(targetRoot,targetDir,appinfo.name)
    if not os.path.exists(targetDir):
        os.makedirs(targetDir, exist_ok=True)
    
    sourceDir = os.path.join(sourceRoot, appinfo.name,fileDir)
    # shutil.copyfile()
    docopy(sourceDir, targetDir, appinfo.fileNames)


def docopy(source, dest, fileNames):
    for name in fileNames:
        join = os.path.join
        file1 = name + '.pdb'
        file2 = name + '.dll'
        shutil.copy2(join(source, file1), join(dest, file1))
        shutil.copy2(join(source, file2), join(dest, file2))
    
    


if __name__ == '__main__':
    # sourceRoot = r'D:\Teams\iExchangeCollection\iExchange3 Team\iExchange3Promotion'
    copy()
    print('done')
    
    
    
