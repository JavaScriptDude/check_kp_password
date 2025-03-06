# Simple example of how to check keepass passwords using pykeepass library
# This was tested against a kdbx4 file generated using KeepassXC on linux
# To test, generate a kdpbx4 file in the same directory named passwords_kdbx4.kdbx
# and set the password to testpassword123

# svc_root: <py_root>/other/keepass/check_kp_password/
# homepage: https://github.com/JavaScriptDude/check_kp_password

# Install dependencies: 
#   % python3 -m pip install pykeepass
# running: 
#   % python3 check_kp_password.py

import os.path, sys
from pykeepass import PyKeePass

def main():

    file = './passwords_kdbx4.kdbx'

    passwords = ['wrong1', 'wrong2', 'testpassword123', 'wrong3']

    if not os.path.isfile(file):
        exit(f'File not found: {file}', 1)
        return

    for password in passwords:

        try:
            kp = PyKeePass(file, password=password)
            exit(f"Success - Password is {password}")

        except Exception as ex:
            print(f"fail: {password} ...")


def exit(msg, code=0):
    print(msg)
    sys.exit(code)

if __name__=='__main__':
    main()