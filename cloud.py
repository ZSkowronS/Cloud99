import ptvsd
ptvsd.enable_attach(secret = 'zaq12WSX', address = ('0.0.0.0', 8080))

import sys
from cloud99.cli.commands import cli

if __name__ == '__main__':
    result = cli();
    sys.exit(result)
