import subprocess
import sys
import os


dirs = {
    "ws3191": r"\\ws3191\Products\iExchange\TransactionService",
    "ws3193":r"\\ws3193\iExchange\TransactionService",
    'ws3195':r'\\ws3195\Products\iExchange\TransactionService',
    "z": r"Z:\Common\SwapFiles\Robert",
    "server": r'D:\work\outterServerLoginInfo\name.txt',
    "dump":r"D:\iExchange\DumpTool"
}


if __name__ == "__main__":
    target = sys.argv[1]
    isfile = sys.argv[2] if len(sys.argv) > 2 else 0
    print(isfile)
    if isfile == 0:
        subprocess.Popen('explorer "%s"' % dirs[target],shell=True)
    else:
        os.startfile(dirs[target])
        # subprocess.Popen(r'explorer /select,"%s"' % dirs[target],shell=True)
        
