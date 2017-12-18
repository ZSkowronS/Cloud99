from __future__ import print_function

import sys
sys.path.append("pycharm-debug.egg")

print("Before attach.")

import pydevd
pydevd.settrace('localhost', port=8080, stdoutToServer=True, stderrToServer=True)

print("Attached.")

import sys
#from cloud99.cli.commands import cli

x = 5
if __name__ == '__main__':
    #result = cli();
    #sys.exit(result)
    print("Ola prola.")
