# Калькулятор времени. Напишите программу, которая просит пользователя ввести
# количество секунд и работает следующим образом.
# • В минуте 60 секунд. Если число введенных пользователем секунд больше или равно
# 60, то программа должна преобразовать число секунд в минуты и секунды.
# • В часе 3 600 секунд. Если число введенных пользователем секунд больше или равно
# 3 600, то программа должна преобразовать число секунд в часы, минуты и секунды.
# • В дне 86 400 секунд. Если число введенных пользователем секунд больше или равно
# 86 400, то программа должна преобразовать число секунд в дни, часы, минуты и
# секунды.
# Time Calculator
secondsInput = abs(int(input("Enter a number of seconds: ")))
if secondsInput < 60:
    days = 0
    hours = 0
    minutes = 0
    seconds = secondsInput
#    print("Time:", days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')
elif 60 <= secondsInput < 3600:
    days = 0
    hours = 0
    minutes = secondsInput // 60
    seconds = secondsInput % 60
#    print("Time:", days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')
elif 3600 <= secondsInput < 86400:
    days = 0
    hours = secondsInput // 3600
    secondsLeft = secondsInput % 3600
    if secondsLeft > 60:
        minutes = secondsLeft // 60
        seconds = secondsLeft % 60
    else:
        minutes = 0
        seconds = secondsLeft
#    print("Time:", days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds')
else:
    days = secondsInput // 86400
    secondsLeft = secondsInput % 86400
    if secondsLeft >= 3600:
        hours = secondsLeft // 3600
        secondsForMinLeft = secondsLeft % 3600
        if secondsForMinLeft >= 60:
            minutes = secondsForMinLeft // 60
            seconds = secondsForMinLeft % 60
        else:
            minutes = 0
            seconds = secondsForMinLeft
    elif 60 <= secondsLeft < 3600:
        hours = 0
        minutes = secondsLeft // 60
        seconds = secondsLeft % 60
    else:
        hours = 0
        minutes = 0
        seconds = secondsLeft
if seconds < 2:
    secondsPrint = 'second'
else:
    secondsPrint = 'seconds'
if minutes < 2:
    minutesPrint = 'minute'
else:
    minutesPrint = 'minutes'
if hours < 2:
    hoursPrint = 'hour'
else:
    hoursPrint = 'hours'
if days < 2:
    daysPrint = 'day'
else:
    daysPrint = 'days'
print("Time:", days, daysPrint, hours, hoursPrint, minutes, minutesPrint, seconds, secondsPrint)
