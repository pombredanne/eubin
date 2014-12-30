#!/usr/bin/env python3

from zipfile import ZipFile
import os
import glob

ZIPFILE = 'bin/eubin.zip'
BINFILE = 'bin/eubin'
MAIN_SCRIPT = b'''\
from eubin import main
if __name__ == "__main__":
    main.main()
'''

# chdir
filedir = os.path.dirname(__file__)
os.chdir(os.path.join(filedir, '..'))

# Bundling modules
with ZipFile(ZIPFILE, mode='w') as zipfile:
    for path in glob.glob('eubin/*.py'):
        zipfile.write(path)

    # Define entry point
    zipfile.writestr('__main__.py', MAIN_SCRIPT)

# Generate executable
with open(BINFILE, 'wb') as fw:
    fw.write(b'#!/usr/bin/env python3\n')
    fw.write(open(ZIPFILE, 'rb').read())

os.chmod(BINFILE, 0o755)
os.remove(ZIPFILE)

print('Executable:', BINFILE)
