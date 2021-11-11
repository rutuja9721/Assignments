#Write a python program that check date and time and
#triggers a subprocess (say assignment 62) at a particular time
#and prints output from child process

import subprocess
from subprocess import Popen,PIPE
import datetime

# subprocess.run('dir', shell=True)

time = datetime.datetime.strptime("03/02/21 10:30", "%d/%m/%y %H:%M")

x = datetime.datetime.now().time().hour

if(time.hour == x):
    s = subprocess.run("python C:\\Users\dell\PycharmProjects\Python_assignments\Assignment6.py", shell=True)
    # print(s.decode("utf-8"))

else:
    print("Time out")
