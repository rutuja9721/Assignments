#Read file country data and calculate average population by continent

file1 =open("D:\PythonWork\PythonWork\Data\countrydata.txt","r")

lines = file1.readlines()
result = []
for line in lines:
    result.append(line.split('\t'))

sumAsia = 0
sumAfrica = 0
sumEurope = 0
sumAmericas = 0
sumOceania = 0

countAsia = 0
countAfrica = 0
countEurope = 0
countAmericas = 0
countOceania = 0

for i in result[1:]:
    if(i[2] == 'Asia'):
        sumAsia = sumAsia + int(i[3])
        countAsia = countAsia + 1
    elif (i[2] == 'Africa'):
        sumAfrica = sumAfrica + int(i[3])
        countAfrica = countAfrica + 1
    elif (i[2] == 'Europe'):
        sumEurope = sumEurope + int(i[3])
        countEurope = countEurope + 1
    if (i[2] == 'Americas'):
        sumAmericas = sumAmericas + int(i[3])
        countAmericas = countAmericas + 1
    if (i[2] == 'Oceania'):
        sumOceania = sumOceania + int(i[3])
        countOceania = countOceania + 1

print("Average population of Asia : " + str(sumAsia/countAsia))
print("Average population of Africa : " + str(sumAfrica/countAfrica))
print("Average population of Europe : " + str(sumEurope/countEurope))
print("Average population of Americas : " + str(sumAmericas/countAmericas))
print("Average population of Oceania : " + str(sumOceania/countOceania))
