# securities trading
numberOfSharesPurchased = 2000
pricePerSharePurchased = 40.00
commissionRateForStockPurchased = 0.03
amountStockPurchased = numberOfSharesPurchased * pricePerSharePurchased
commissionPaidForStockPurchased = amountStockPurchased * commissionRateForStockPurchased
numberOfSharesSold = 2000
pricePerShareSold = 42.75
commissionRateForStockSold = 0.03
amountStockSold = numberOfSharesSold * pricePerShareSold
commissionPaidForStockSold = amountStockSold * commissionRateForStockSold
commissionTotal: float = commissionPaidForStockSold + commissionPaidForStockPurchased
operationBottomLine: float = amountStockSold - amountStockPurchased - commissionTotal
print("Buying", numberOfSharesPurchased, "shares for", pricePerSharePurchased, "UAH Joe paid",
      format(amountStockPurchased, '.2f'), "UAH and", format(commissionPaidForStockPurchased, '.2f'),
      "UAH as a commission.\nWhen selling", numberOfSharesSold, "shares for", pricePerShareSold, "UAH, he got",
      format(amountStockSold, '.2f'), "UAH, but paid", format(commissionPaidForStockSold, '.2f'),
      "UAH as a commission.")
if operationBottomLine >= 0:
    if operationBottomLine > 0:
        print("As a result of trading Joe made a profit of", format(operationBottomLine, '.2f'), "UAH.")
    else:
        print("Joe reached break-even point with this particular trade.")
else:
    print("As a result of trading Joe made a loss of", format((abs(operationBottomLine)), '.2f'), "UAH.")
