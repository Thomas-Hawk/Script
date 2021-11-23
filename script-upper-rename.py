import os

list = os.listdir('.')

for name in list:
    if name != "script.py":
        old_name = os.path.join('.',''+name+'')
        new_name = os.path.join('.',''+name.upper()+'')
        print (old_name, new_name)
        os.rename(old_name, new_name)
