def isPrime(num):
    y = 0
    for x in range (1, num+1):
        if num % x == 0:
            y += 1
            if y > 2:
                return False
    return True
