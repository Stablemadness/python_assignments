start = "some + words"
day = "TueSday"
#def add_time(start, duration, day=""):
days = ["Monday", "Tuesday", "Wednesday", "Thursday"
        , "Friday", "Saturday", "Sunday"]

#    timesplit
startsplit = start.split()
start_time = startsplit[0].split(':')
if startsplit[1] == 'PM':
    PM = True
else:
    PM = False
days_lower = days.copy()
print(days_lower)
for i in range(len(days_lower)):
    days_lower[i] = days_lower[i].lower()

print(days_lower)
day = day.lower()
print(days_lower.index(day))
