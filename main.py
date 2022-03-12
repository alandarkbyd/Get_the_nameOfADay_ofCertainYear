monthCodes = {    
	'1' : 0,
  '2' : 3,
  '3' : 3,
  '4' : 6,
  '5' : 1,
  '6' : 4,
  '7' : 6,
  '8' : 2,
  '9' : 5,
  '10' : 0,
  '11' : 3,
  '12' : 5,
}

dayNames = {
	'0' : 'Sunday',
	'1' : 'Monday',
	'2' : 'Tuesday',
	'3' : 'Wednesday',
	'4' : 'Thursday',
	'5' : 'Friday',
	'6' : 'Saturday'
}

# year = ('2022')
# month = '3'
# day = '13'
day, month, year = input('Enter the date (24.9.2021): ').split('.')

CenturyC = 0
if int(year) in range(1700, 1799):
	CenturyC = 4
elif int(year) in range(1800, 1899):
	CenturyC = 2
elif int(year) in range(1900, 1999):
	CenturyC = 0
elif int(year) in range(2000, 2099):
	CenturyC = 6
elif int(year) in range(2100, 2199):
	CenturyC = 4
elif int(year) in range(2200, 2299):
	CenturyC = 2
elif int(year) in range(2300, 2399):
	CenturyC = 0

	

leapYearCode = 0
if int(year)%4 == 0 or int(year)%400 == 0:
	leapYearCode = 1
	
yearCode = (int(year[2:])+(int(year[2:])//4))%7

result = (yearCode + monthCodes[month] + CenturyC + int(day) - leapYearCode)%7
print('The name of the day is:',dayNames[str(result)])
