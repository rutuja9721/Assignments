#Get MaxDate, MinDate, InputFile name as command line arguments
#Read tran_dtl file (file name as command arg), filter data between MaxDate and MinDate
#and Aggregate total Sales by Product

#tran_dtl file used here is a text file available in the folder

import sys
import datetime
from itertools import groupby

maxdate = datetime.datetime.strptime(sys.argv[2], '%Y/%m/%d')
mindate = datetime.datetime.strptime(sys.argv[1],'%Y/%m/%d')

file1 = open(sys.argv[3],"r")

#lines = [line[:-1] for line in file1]

lines = file1.read().splitlines()
# lines = file1.readlines()[:-1]

lines2 = []
lines3 = []

for line in lines:
    lines2.append(line.split('\t'))

# date1 = datetime.datetime.strptime(lines2[1][4],'%m-%d-%Y')

lines2.sort(key = lambda x:int(x[1]))

for j, group in groupby(lines2, key=lambda x:int(x[1])):
    if (datetime.datetime.strptime(lines2[j][4], '%m-%d-%Y') > datetime.datetime.strptime(sys.argv[1],'%Y/%m/%d') and datetime.datetime.strptime(lines2[j][4], '%m-%d-%Y') < datetime.datetime.strptime(sys.argv[2], '%Y/%m/%d')):
        lines3.append([j, sum(float(i[3]) for i in group)])

print(lines3)

