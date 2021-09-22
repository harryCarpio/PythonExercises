# Write a Python program to get the size, permissions, owner, device, created, last modified, and last accessed date time of a specified path.
import os
import time
import platform
from pathlib import Path

path = 'C:/Users/harry/Videos/2021-06-07 01-01-57.mkv'

size = os.path.getsize(path)
print("Path size: {} bytes".format(size))

read_permission = os.access(path, os.R_OK) # Check for read access
write_permission = os.access(path, os.W_OK) # Check for read access
exec_permission = os.access(path, os.X_OK) # Check for read access
print("Permissions: R:{}, W:{}, X: {}".format(read_permission, write_permission, exec_permission))

info = Path(path)
print("Owner: ")
##print("Owner: {}".format(info.owner()))


if platform.system() == "Windows":
    print("Device: {}".format(platform.uname().node))
else:
    print("Device: {}".format(os.uname()[1]))

created = os.path.getctime(path)
created_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created))
print("Created: {}".format(created_str))


last_modified = os.path.getmtime(path)
last_modified_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))
print("Last modified: {}".format(last_modified_str))

last_access = os.path.getatime(path)
last_access_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_access))
print("Last access: {}".format(last_access_str))
