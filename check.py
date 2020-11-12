#!/usr/bin/env python3
# Python 3.8.5
'''
Change log:
    Oct 28, 2020 (v1.3): allow empty sid directory in the zip file
    Oct 26, 2020 (v1.2): the sid directory could be omitted
    Oct 25, 2020 (v1.1): be lenient about zip filenames
    Oct 23, 2020 (v1.0): enjoy my horrible coding styles :P
'''

import sys
assert sys.version >= '3.6', 'this script will be run with at least python3.6'
import re
from zipfile import ZipFile
from pathlib import Path

'''
myzipfile.zip
└── r12345678
    ├── code
    │   ├── alice
    │   │   └── bob
    │   ├── bar.js
    │   └── foo.py
    └── writeup.pdf
'''


if len(sys.argv) < 2:
    print ('usage: python3 check.py <path/to/your/zipfile.zip>')
    exit(0)

zip_filepath = Path(sys.argv[1])
assert zip_filepath.name.endswith('.zip'), 'The filename should be *.zip'

zip_file = ZipFile(zip_filepath)
has_pdf = False
has_code = False
has_error = False
sid = ''
for name in zip_file.namelist():
    if sid == '':
        sid = name.split('/')[0]
    path = Path(name)
    if path == Path(sid) / '':
        continue
    if path == Path(sid) / 'writeup.pdf':
        has_pdf = True
        continue
    if path == Path(sid) / 'code':
        has_code = True
        continue
    if Path(sid) / 'code' in path.parents:
        if any(re.match(r, path.name) for r in r'''
node_modules
__pycache__
.*\.pyc
.*\.i64
.*\.idb
'''.strip().splitlines()):
            print('Please do not zip this file:', path)
            has_error = True
        continue
    print('Invalid file:', path)
    has_error = True

if not has_pdf:
    print('writeup.pdf is missing!')
    has_error = True
if not has_code:
    print('code/ directory is missing!')
    has_error = True
if sid != sid.lower():
    print('Student ID shoud be in lowercase!')
    has_error = True

if has_error:
    print('''
Some errors occur! Your homework will be degraded! Please fix it.
To compress a zip file without __MACOSX and .DS_Store, see https://stackoverflow.com/a/13665552/11712282
'''.strip())
else:
    print('Sanity check passed')