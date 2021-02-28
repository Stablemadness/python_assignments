def add_time(start, duration, day=""):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday"
            , "Friday", "Saturday", "Sunday"]

    day = day.capitalize()

    start_split = start.split()
    start_time = start_split[0].split(':')
    dur_split = duration.split(':')
    d_hours = int(dur_split[0])
    d_mins = int(dur_split[1])
    start_mins = int(start_time[1])
    start_hour = int(start_time[0])
    if start_split[1] == 'PM':
        PM = True
    else:
        PM = False

    total_mins = start_mins + d_mins
    if total_mins >= 60:
        minutes = total_mins % 60
        d_hours += 1
    else:
        minutes = total_mins

    day_cross = 0
    while d_hours > 0:
        d_hours -= 1
        start_hour += 1
        if start_hour % 12 == 0:
            start_hour = 0
            if PM:
                day_cross += 1
                PM = not PM
            else:
                PM = not PM

    if start_hour == 0:
        start_hour = 12
    else:
        start_hour = start_hour % 12

    new_day = ""
    if day != '':
        x = days.index(day)
        day_index = (x + day_cross) % 7
        new_day = days[day_index]

    new_time = ''
    if minutes < 10:
        minutes = "0" + str(minutes)
#    if start_hour < 10:
#        new_time = "0" + str(start_hour) + ":" + str(minutes)
#    else:
    new_time = str(start_hour) + ":" + str(minutes)
    if PM:
        new_time = new_time + " PM"
    else:
        new_time = new_time + " AM"

    if day != "":
        if day_cross == 0:
            new_time = new_time + ", " + new_day
        elif day_cross == 1:
            new_time = new_time + ", " + new_day + " (next day)"
        else:
            new_time = new_time + ", " + new_day + " (" + str(day_cross) + " days later)"
    else:
        if day_cross == 0:
            new_time = new_time
        elif day_cross == 1:
            new_time = new_time + " (next day)"
        else:
            new_time = new_time + " (" + str(day_cross) + " days later)"
    return new_time


print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "Tuesday"))
# Returns: 12:03 AM, Thursday (2 days later)

actual = add_time("3:30 PM", "2:12")
print(actual)

actual = add_time("11:55 AM", "3:12")
print(actual)
print("expected = \"3:07 PM")
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

actual = add_time("9:15 PM", "5:30")
print(actual)
print("expected = \"2:45 AM (next day)")
#        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

actual = add_time("11:40 AM", "0:25")
print(actual)
print("expected = \"12:05 PM")
#        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

actual = add_time("2:59 AM", "24:00")
print(actual)
print("expected = \"2:59 AM (next day)")
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

actual = add_time("11:59 PM", "24:05")
print(actual)
print("expected = \"12:04 AM (2 days later)")
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')


actual = add_time("8:16 PM", "466:02")
print(actual)
#        expected = "6:18 AM (20 days later)"
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

actual = add_time("5:01 AM", "0:00")
print(actual)
#        expected = "5:01 AM"
#        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')


actual = add_time("3:30 PM", "2:12", "Monday")
print(actual)
#        expected = "5:42 PM, Monday"
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')


actual = add_time("2:59 AM", "24:00", "saturDay")
print(actual)
#        expected = "2:59 AM, Sunday (next day)"
#        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

actual = add_time("11:59 PM", "24:05", "Wednesday")
print(actual)
#        expected = "12:04 AM, Friday (2 days later)"


actual = add_time("8:16 PM", "466:02", "tuesday")
print(actual)
#        expected = "6:18 AM, Monday (20 days later)"
