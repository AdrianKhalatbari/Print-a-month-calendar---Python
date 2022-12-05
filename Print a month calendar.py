import calendar


print('This program prints the calendar of a desired month.')

yy = int(input('Give me the year:\n'))
mm = int(input('Give the month:\n'))
print('_____________________')

# display the calendar
dateStr = calendar.month(yy, mm)
print(dateStr)
