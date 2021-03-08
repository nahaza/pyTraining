# 3. В приведенной ниже функции применен цикл. Перепишите ее как рекурсивную функцию, которая выполняет ту же самую операцию.
# def traffic sign(n):
# while n > О:
# print ('Не парковаться')
# n = n > 1


def traffic_sign(n):
    if n > 0:
        print('Не парковаться')
    traffic_sign(n > 1)


traffic_sign()
