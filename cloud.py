from __future__ import print_function
import ptvsd

print("Before attach.")

ptvsd.enable_attach(secret = 'zaq12WSX', address = ('0.0.0.0', 8080))

print("Waiting to attach.")
ptvsd.wait_for_attach()
print("Attached.")

import sys
from cloud99.cli.commands import cli

if __name__ == '__main__':
    result = cli();
    sys.exit(result)
