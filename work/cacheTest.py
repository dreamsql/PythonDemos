




import re

import os









path = r'D:\Programming\C#\CacheBuffer\Facade\bin\Debug\Logs\mylogfile.txt'

cachefiledir = r'D:\Programming\C#\CacheBuffer\Facade\bin\Debug\CacheFiles'


def parseAccountAndVersion():
    cachefiles = set()
    pattern = r'DeleteCacheFile\s.*?\\(.*)'
    with open(path) as f:
        for line in f :
            m = re.search(pattern, line)
            if m:
                cachefiles.add(m.group(1))
    return cachefiles
 

def get_all_cache_files():
    return [ file for file in os.listdir(cachefiledir) if os.path.isfile(os.path.join(cachefiledir, file))]
     


if __name__ == '__main__':
    deletedfiles = parseAccountAndVersion()
    unsavedfiles = get_all_cache_files()
    print('deletedfiles.count = {}, unsavedfiles.count = {}'.format(len(deletedfiles), len(unsavedfiles)))
    for f in unsavedfiles:
        if f not in deletedfiles:
            print('undeleted file = {}'.format(f))






















