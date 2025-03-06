Simple example of how to check keepass passwords using pykeepass library.

This was tested against a kdbx4 file generated using KeepassXC on linux.

To test, generate a kdpbx4 file in the same directory named passwords_kdbx4.kdbx and set the password to testpassword123.

Install dependencies: 
```% python3 -m pip install pykeepass```

running: 
```% python3 check_kp_password.py```
