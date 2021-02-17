# Sales prediction
grossProfitMargin = 0.23
salesProjections = float(input("Enter your sales projections, UAH: "))
profitProjections = salesProjections*grossProfitMargin
print("Your projected gross profit, UAH: ", format(profitProjections, '.2f'))
