# 1. Bug Collector
# A bug collector collects bugs every day for five days. Write a program that keeps a running
# total of the number of bugs collected during the five days. The loop should ask for the
# number of bugs collected for each day, and when the loop is finished, the program should
# display the total number of bugs collected.

total = 0
i = 1
days = 5
while i <= days:
    numOfBugs = int(input("Enter a number of bugs collected: "))
    i += 1
    total += numOfBugs
print("The number of bugs collected for", days, 'days =', total)

# Alternative answer
total = 0
days = 5
for i in range(1, days+1):
    numOfBugs = int(input("Enter a number of bugs collected for day " + str(i) + ': '))
    i += 1
    total += numOfBugs
print("The number of bugs collected for", days, 'days =', total)