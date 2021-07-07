import calendar

weekday = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

m, d, y = map(int, input('Enter the date = ').split())

p = calendar.weekday(y, m, d)

print(weekday[p])
