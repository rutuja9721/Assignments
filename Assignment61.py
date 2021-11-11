#Get MaxDate, numDays, inputFile as command line argument,
#Findout minDate as MaxDate minus numDays, read trandtl File and
#calculate aggregate sale by product

import sys
import datetime
from itertools import groupby
from datetime import timedelta

maxdate = datetime.datetime.strptime(sys.argv[2], '%Y/%m/%d')
no_day = int(sys.argv[1])

file1 = open(sys.argv[3],"r")

#lines = [line[:-1] for line in file1]
mindate = maxdate - timedelta(days = no_day)

lines = file1.read().splitlines()
# lines = file1.readlines()[:-1]

lines2 = []
lines3 = []

for line in lines:
    lines2.append(line.split('\t'))

lines2.sort(key = lambda x:int(x[1]))

for j, group in groupby(lines2, key=lambda x:int(x[1])):
    if (datetime.datetime.strptime(lines2[j][4], '%m-%d-%Y') > mindate and datetime.datetime.strptime(lines2[j][4], '%m-%d-%Y') < datetime.datetime.strptime(sys.argv[2], '%Y/%m/%d')):
        lines3.append([j, sum(float(i[3]) for i in group)])

print(lines3)