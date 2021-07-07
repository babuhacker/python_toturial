import calendar

weekday = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

m, d, y = map(int, input().split())

p = calendar.weekday(y, m, d)

print(weekday[p])
