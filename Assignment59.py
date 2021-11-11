#Get Date as command line argument
#Calculate Day of the month, day of the year, week of the year for the date and print the same
import datetime
import sys

date = datetime.datetime.strptime(sys.argv[1], '%y-%m-%d')

print("Day : " + str(date.day))
print("Month : " + str(date.month))
print("Year : " + str(date.year))