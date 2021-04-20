import sys
import requests
import time
import os

print(sys.argv[1])
n = int(sys.argv[1])

for i in range(n):
    os.popen("curl http://localhost:4440")


